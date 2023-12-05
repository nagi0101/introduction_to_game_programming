import unittest
from typing import List

from math import pi
from Utils.Vector import Vec3
from Utils.Rotator import Rot3


class VectorTest(unittest.TestCase):
    def assert_vec3(self, v:Vec3, a:List):
        self.assertAlmostEqual(v.x, a[0], places=6)
        self.assertAlmostEqual(v.y, a[1], places=6)
        self.assertAlmostEqual(v.z, a[2], places=6)
    
    def test_Vec3(self):
        v = 0.5 * Vec3(1.0, -1.0, 0.5)
        self.assert_vec3(v, [0.5, -0.5, 0.25])
        
        v = Rot3(roll=0, pitch=0, yaw=pi * 0.5).rotate_vec3(Vec3(1, 0, 0))
        self.assert_vec3(v, [0.0, 0.0, -1.0])
        
        v = Rot3(-pi * 0.5, 0, 0).rotate_vec3(Vec3(1, 0, 0))
        self.assert_vec3(v, [0.0, -1.0, 0.0])
        
        v = Rot3(0, -pi * 0.5, 0).rotate_vec3(Vec3(1, 0, 0))
        self.assert_vec3(v, [1.0, 0.0, 0.0])
        
        v0 = Rot3(pi * 0.25, 0, pi * 0.25).rotate_vec3(Vec3(1, 0, 0))
        v1 = Rot3(pi * 0.25, 0, 0).rotate_vec3(Vec3(1, 0, 0))
        v1 = Rot3(0, 0, pi * 0.25).rotate_vec3(v1)
        self.assert_vec3(v0, [v1.x, v1.y, v1.z])
        
        # Vec3 lerp test
        v = Vec3.lerp(Vec3(1.0, 1.0, 1.0), Vec3(0.0, 0.0, 0.0), 0.0)
        self.assert_vec3(v, [1.0, 1.0, 1.0])
        
        v = Vec3.lerp(Vec3(2131, 212.2, 25.1), Vec3(104.0, 165.5, 235.0), 1)
        self.assert_vec3(v, [104.0, 165.5, 235.0])
        
        v = Vec3.lerp(Vec3(1.0, -1.0, 0.0), Vec3(0.0, 0.0, 0.0), 0.5)
        self.assert_vec3(v, [0.5, -0.5, 0.0])
        
        v = Vec3.lerp(Vec3(51.0, -1.0, 0.0), Vec3(0.0, 0.0, 0.0), 0.9)
        self.assert_vec3(v, [5.1, -0.1, 0.0])
        
        v = Vec3.lerp(Vec3(51.0, -1.0, 0.0), Vec3(512.4, 5.7, 2.8), 0.7)
        self.assert_vec3(v, [373.98, 3.69, 1.96])
        
        v = Vec3.lerp(Vec3(1.0, -1.0, 0.0), Vec3(2.0, 3.5, 1.0), -2)
        self.assert_vec3(v, [-1.0, -10.0, -2.0])
        
        
if __name__ == '__main__':
    unittest.main()
    