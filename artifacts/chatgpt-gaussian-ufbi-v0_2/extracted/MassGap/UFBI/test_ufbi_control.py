import unittest
import numpy as np
from scipy.sparse import diags
from ufbi_control import Geometry, GaussianBox, evaluate

class TestGaussianUFBI(unittest.TestCase):
    def test_dst_operator_against_dense_tiny_grid(self):
        g=Geometry(1,3,2)
        box=GaussianBox(g)
        n=g.L
        d=diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1]).toarray()
        i=np.eye(n)
        a=np.zeros((n**4,n**4))
        for axis in range(4):
            blocks=[d if j==axis else i for j in range(4)]
            z=blocks[0]
            for b in blocks[1:]: z=np.kron(z,b)
            a+=z
        a+=g.m0**2*np.eye(n**4)
        rng=np.random.default_rng(4)
        v=rng.normal(size=(n,)*4)
        np.testing.assert_allclose(box.inv(v).ravel(),np.linalg.solve(a,v.ravel()),atol=1e-11,rtol=1e-11)
    def test_identical_collars_zero_distance(self):
        box=GaussianBox(Geometry(2,3,2))
        d,_=box.mahalanobis(np.zeros(box.n),'full')
        self.assertEqual(d,0.)
    def test_data_processing_order(self):
        results={v['observable']:v for v in evaluate(Geometry(2,3,2),full=True)}
        self.assertLessEqual(results['mean']['dM'],results['moments']['dM']+1e-9)
        self.assertLessEqual(results['moments']['dM'],results['full']['dM']+1e-9)
    def test_boundary_source_linear(self):
        box=GaussianBox(Geometry(2,3,2))
        np.testing.assert_allclose(box.source('constant',2),2*box.source('constant',1))
    def test_mass_and_geometry_guard(self):
        with self.assertRaises(ValueError): Geometry(2,4,2)
        with self.assertRaises(ValueError): Geometry(2,3,0)

if __name__=='__main__': unittest.main()
