import unittest
from .vector import Vector, Line


class TestVector(unittest.TestCase):
    def test_length(self):
        self.assertEqual(Vector(3, 4).length(), 5)

    def test_mul_scalar(self):
        v2 = Vector(3, 4) * 2
        self.assertEqual(v2.x, 6)
        self.assertEqual(v2.y, 8)

    def test_rmul_scalar(self):
        v2 = 2 * Vector(3, 4)
        self.assertEqual(v2.x, 6)
        self.assertEqual(v2.y, 8)

    def test_dot_product(self):
        self.assertEqual(Vector(1, 2) * Vector(3, 4), 11)

    def test_div(self):
        v2 = Vector(2, 4) / 2
        self.assertEqual(v2.x, 1)
        self.assertEqual(v2.y, 2)

    def test_norm(self):
        v2 = Vector(3, 4).normalized()
        self.assertAlmostEqual(v2.x, 0.6)
        self.assertAlmostEqual(v2.y, 0.8)

    def test_add(self):
        v2 = Vector(1, 2) + Vector(3, 4)
        self.assertEqual(v2.x, 4)
        self.assertEqual(v2.y, 6)

    def test_sub(self):
        v2 = Vector(4, 3) - Vector(1, 2)
        self.assertEqual(v2.x, 3)
        self.assertEqual(v2.y, 1)

    def test_normal_to(self):
        v1 = Vector(4, 3)
        v2 = v1.normal_to()

        self.assertAlmostEqual(v1.length(), v2.length())
        self.assertAlmostEqual(v1 * v2, 0)


class TestLine(unittest.TestCase):

    def test_intersection(self):
        l1 = Line(Vector(2, 5), Vector(3, 2))
        l2 = Line(Vector(8, 3), Vector(-3, 4))
        i = l1.intersection_with(l2)
        self.assertEqual(i.x, 5)
        self.assertEqual(i.y, 7)
