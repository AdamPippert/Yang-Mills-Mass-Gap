#!/usr/bin/env python3
"""Four-dimensional free-scalar UFBI control. Numerical evidence, not proof.

Units: central physical side q=1, lattice spacing a=q/B, outer side R*q,
physical mass m, scalar lattice-field phi=a*Phi (4D canonical scaling).
Ghost boundary values are held fixed and enter as source on adjacent sites.
"""
from __future__ import annotations
import argparse
import csv
from dataclasses import dataclass
import itertools
import math
from pathlib import Path

import numpy as np
from scipy.fft import dstn
from scipy.sparse.linalg import LinearOperator, cg
from scipy.special import erf

@dataclass(frozen=True)
class Geometry:
    B: int
    R: int
    mass: float
    q: float = 1.0
    def __post_init__(self):
        if self.B < 1 or self.R < 3 or self.R % 2 == 0 or self.mass <= 0 or self.q <= 0:
            raise ValueError('B>=1, odd R>=3, mass>0 and q>0 required')
    @property
    def L(self): return self.R * self.B
    @property
    def a(self): return self.q / self.B
    @property
    def m0(self): return self.mass * self.a
    @property
    def distance(self):
        # nearest occupied central node to closest exterior ghost node
        return (((self.R - 1) // 2) * self.B + 1) * self.a
    @property
    def qslice(self):
        start = ((self.R - 1) // 2) * self.B
        return (slice(start,start+self.B),)*4

class GaussianBox:
    def __init__(self, g:Geometry):
        self.g=g
        k=np.arange(1,g.L+1,dtype=float)
        lam=2*(1-np.cos(np.pi*k/(g.L+1)))
        self.inv_eigs=1.0/(lam[:,None,None,None]+lam[None,:,None,None]+lam[None,None,:,None]+lam[None,None,None,:]+g.m0**2)
        self.shape=(g.L,)*4
        self.qshape=(g.B,)*4
        self.qslice=g.qslice
        self.n=g.B**4
    def inv(self,v):
        if v.shape != self.shape: raise ValueError('wrong full-grid shape')
        return dstn(dstn(v,type=1,norm='ortho')*self.inv_eigs,type=1,norm='ortho')
    def embed(self,x):
        buf=np.zeros(self.shape)
        buf[self.qslice]=np.asarray(x).reshape(self.qshape)
        return buf
    def sigma_q(self,x):
        return self.inv(self.embed(x))[self.qslice].ravel()
    def source(self,pattern:str,amplitude:float,seed:int=0):
        """Difference source from collars with tau=pattern, tau'=-pattern.
        Every face contributes one external link; intersections contribute independently.
        amplitude is a physical continuum field amplitude, so phi=a*amplitude.
        """
        g=self.g
        rng=np.random.default_rng(seed)
        b=np.zeros(self.shape)
        for axis in range(4):
            for side in (0,g.L-1):
                face_shape=(g.L,)*3
                if pattern=='constant': face=np.ones(face_shape)
                elif pattern=='random': face=rng.choice([-1.,1.],size=face_shape)
                elif pattern=='checkerboard': face=(-1.)**np.indices(face_shape).sum(axis=0)
                elif pattern=='face': face=np.ones(face_shape) if axis==0 and side==0 else np.zeros(face_shape)
                else: raise ValueError('pattern must be constant, random, checkerboard or face')
                index=[slice(None)]*4;index[axis]=side
                b[tuple(index)]+=2*g.a*amplitude*face
        return b
    def mean_shift(self,source):
        return self.inv(source)[self.qslice].ravel()
    def modes(self,kind:str):
        """Rows are linear measurement kernels on Q. Normalization of a row
        does not affect the TV of its nondegenerate Gaussian output."""
        if kind=='mean': return np.ones((1,self.n))/self.n
        if kind=='moments':
            idx=np.indices(self.qshape,dtype=float)
            modes=[np.ones(self.qshape)]
            if self.g.B>1:
                for ax in range(4): modes.append(idx[ax]-(self.g.B-1)/2)
            return np.stack([v.ravel()/np.linalg.norm(v) for v in modes])
        raise ValueError('mean or moments expected')
    def mahalanobis(self,shift,kind='full',tol=1e-9):
        if kind=='full':
            operator=LinearOperator((self.n,self.n),matvec=self.sigma_q,dtype=float)
            x,info=cg(operator,shift,rtol=tol,atol=0,maxiter=1500)
            rel=np.linalg.norm(self.sigma_q(x)-shift)/max(np.linalg.norm(shift),1e-30)
            if info!=0 or rel>max(10*tol,1e-7):
                raise RuntimeError(f'CG failed: info={info}, residual={rel:.3g}')
            return math.sqrt(max(float(shift@x),0)),rel
        F=self.modes(kind)
        K=np.stack([self.sigma_q(row) for row in F])
        cov=F@K.T
        cov=(cov+cov.T)/2
        delta=F@shift
        z=np.linalg.solve(cov,delta)
        return math.sqrt(max(float(delta@z),0)),float(np.linalg.cond(cov))

def evaluate(g:Geometry,pattern='constant',amplitude=1.0,seed=0,full=True):
    box=GaussianBox(g)
    shift=box.mean_shift(box.source(pattern,amplitude,seed))
    result=[]
    for kind in (['mean','moments','full'] if full else ['mean','moments']):
        d,diagnostic=box.mahalanobis(shift,kind)
        two_tv=2*float(erf(d/(2*math.sqrt(2))))
        hellinger=math.sqrt(max(0.0,-math.expm1(-d*d/8)))
        result.append(dict(B=g.B,R=g.R,L=g.L,a=g.a,mass=g.mass,q=g.q,
                           separation=g.distance,pattern=pattern,amplitude=amplitude,
                           observable=kind,dM=d,two_tv=two_tv,H=hellinger,
                           solver_diagnostic=diagnostic))
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--B',nargs='+',type=int,default=[2,3,4])
    p.add_argument('--R',nargs='+',type=int,default=[3,5,7])
    p.add_argument('--mass',type=float,default=2.0)
    p.add_argument('--q',type=float,default=1.0)
    p.add_argument('--amplitude',type=float,default=1.0)
    p.add_argument('--patterns',nargs='+',default=['constant','random','checkerboard','face'])
    p.add_argument('--gamma-fraction',type=float,default=0.5,
                   help='candidate decay gamma = fraction * physical mass')
    p.add_argument('--K',type=float,default=4.,help='preregistered test K for 2TV <= min(2,K*amplitude*exp(-gamma*distance))')
    p.add_argument('--no-full',action='store_true')
    p.add_argument('--strict',action='store_true',help='exit nonzero when the sampled candidate fails or none are informative')
    p.add_argument('--out',default='MassGap/UFBI/results.csv')
    args=p.parse_args()
    if args.K<=0 or args.gamma_fraction<=0: p.error('K and gamma fraction must be positive')
    rows=[]
    for B,R,pattern in itertools.product(args.B,args.R,args.patterns):
        g=Geometry(B,R,args.mass,args.q)
        for item in evaluate(g,pattern,args.amplitude,full=not args.no_full):
            gamma=args.gamma_fraction*g.mass
            envelope=min(2.,args.K*args.amplitude*math.exp(-gamma*g.distance))
            item.update(gamma=gamma,K=args.K,envelope=envelope,
                        ratio=item['two_tv']/envelope if envelope>0 else math.inf,
                        passes=item['two_tv'] <= envelope+1e-9,
                        informative=envelope < 2-1e-9)
            rows.append(item)
        print(f'B={B} R={R} collar={pattern}: '+', '.join(f"{r['observable']} 2TV={r['two_tv']:.4f} pass={r['passes']}" for r in rows[-(2 if args.no_full else 3):]),flush=True)
    out=Path(args.out);out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    failures=[r for r in rows if r['informative'] and not r['passes']]
    informative=sum(r['informative'] for r in rows)
    print(f'Wrote {len(rows)} rows to {out}; informative={informative}; failed={len(failures)}. Sampled necessary-condition check, NOT uniform UFBI verification.')
    if args.strict and (failures or not informative):
        raise SystemExit(1)

if __name__=='__main__': main()
