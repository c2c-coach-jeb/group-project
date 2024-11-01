import unittest
import problem2 as primes


class TestIsPrime(unittest.TestCase):

    def test_two_is_prime(self):
        self.assertTrue(primes.is_prime(41))

    def test_three_is_prime(self):
        self.assertTrue(primes.is_prime(37))

    def test_four_is_not_prime(self):
        self.assertTrue(primes.is_prime(12))


if __name__ == '__main__':
    unittest.main()
