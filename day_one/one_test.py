import unittest
import one


class oneTester(unittest.TestCase):
    def test_tune_by(self):
        self.assertEqual(-3, one.tune_by_string(0, '-3'))
        self.assertEqual(3, one.tune_by_string(0, '+3'))

    def test_one_one_one(self):
        res = one.tune(['+1', '+1', '+1'])
        self.assertEqual(3, res)
    def test_one_one_two(self):
        res = one.tune(['+1', '+1', '-2'])
        self.assertEqual(0, res)

    def test_one_two_three(self):
        res = one.tune(['-1', '-2', '-3'])
        self.assertEqual(-6, res)

    def test_twice_freq_tuen(self):
        res = one.dupe_tune(['+1', '-2', '+3', '+1'])
        self.assertEqual(2, res)

if __name__ == '__main__':
    unittest.main()
