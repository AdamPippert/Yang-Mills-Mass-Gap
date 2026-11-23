import time,numpy as np
from scipy.fft import dstn
from scipy.sparse.linalg import LinearOperator,cg
from scipy.special import erf

def calc(R,B,mell):
 L=R*B; a=1/L; k=np.arange(1,L+1,dtype=float); lam=2*(1-np.cos(np.pi*k/(L+1)))
 inv=1/(lam[:,None,None,None]+lam[None,:,None,None]+lam[None,None,:,None]+lam[None,None,None,:]+(mell*a)**2)
 def ap(v):return dstn(dstn(v,type=1,norm='ortho')*inv,type=1,norm='ortho')
 b=np.zeros((L,)*4)
 for j in range(4):
  for side in [0,L-1]:
   ix=[slice(None)]*4;ix[j]=side;b[tuple(ix)]+=2
 dm=ap(b); s=((R-1)//2)*B; q=(slice(s,s+B),)*4; d=dm[q].ravel()
 def mv(x):
  y=np.zeros((L,)*4);y[q]=x.reshape((B,)*4);return ap(y)[q].ravel()
 x,info=cg(LinearOperator((B**4,B**4),matvec=mv),d,rtol=1e-9,maxiter=2000)
 dM=np.sqrt(max(d@x,0));return L,dM,2*erf(dM/(2*np.sqrt(2))),a*dM,2*erf(a*dM/(2*np.sqrt(2))),info
if __name__ == "__main__":
 for m in (6, 12):
  print("m*ell", m, flush=True)
  print("B L d_lat 2TV_lat d_phys 2TV_phys cg_info seconds", flush=True)
  for B in (1, 2, 3, 4, 5, 6, 8, 10):
   t=time.monotonic()
   r=calc(3,B,m)
   print(B, *(f"{v:.6f}" if isinstance(v,float) else v for v in r),
         round(time.monotonic()-t,2), flush=True)
