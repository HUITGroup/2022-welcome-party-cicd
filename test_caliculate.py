import unittest
import caliculate as cal


class TestCaliculate(unittest.TestCase):
    def test_add(self):
        self.assertEqual(cal.add(1, 1), 2)
        self.assertEqual(cal.add(-4, -3), -7)

    def test_sub(self):
        self.assertEqual(cal.sub(1, 1), 0)
        self.assertEqual(cal.sub(-4, -3), -1)

    def test_mul(self):
        self.assertEqual(cal.mul(1, 1), 1)
        self.assertEqual(cal.mul(1, 0), 0)
        self.assertEqual(cal.mul(-4, -3), 12)

    def test_div(self):
        self.assertEqual(cal.div(1, 1), 1)
        self.assertEqual(cal.div(0, 1), 0)
        self.assertEqual(cal.div(-4, -8), 0.5)


if __name__ == '__main__':
    unittest.main()
