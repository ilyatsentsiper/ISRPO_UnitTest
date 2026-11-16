import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5, 10), 50)

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_square(self):
        self.assertEqual(area(7, 7), 49)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5, 4.0), 10.0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5, 10), 30)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(7, 7), 28)

if __name__ == '__main__':
    unittest.main()
