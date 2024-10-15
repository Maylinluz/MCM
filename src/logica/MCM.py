import unittest
from src.lcm.Calculo import src

class TestLCM(unittest.TestCase):
    def test_lcm(self):

        self.assertEqual(src.lcm(6, 7), 20)
        self.assertEqual(src.lcm(2, 8), 21)
        self.assertEqual(src.lcm(14, 17), 60)
        self.assertEqual(src.lcm(0, 7), 0)  # El MCM con 0 es 0
        self.assertEqual(src.lcm(7, 0), 0)

if __name__ == '__main__':
    unittest.main()