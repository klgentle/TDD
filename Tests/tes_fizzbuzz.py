import unittest
from FizzBuzz import FizzBuzz


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        a = FizzBuzz()
        self.assertEqual(a.fizzbuzz(1), "1")
        self.assertEqual(a.fizzbuzz(2), "2")
        self.assertEqual(a.fizzbuzz(4), "4")

    def test_divide_3(self):
        a = FizzBuzz()
        self.assertEqual(a.fizzbuzz(3), "Fizz")
        self.assertEqual(a.fizzbuzz(6), "Fizz")
        self.assertEqual(a.fizzbuzz(9), "Fizz")

    def test_divide_5(self):
        a = FizzBuzz()
        self.assertEqual(a.fizzbuzz(5), "Buzz")
        self.assertEqual(a.fizzbuzz(10), "Buzz")
        self.assertEqual(a.fizzbuzz(20), "Buzz")

    def test_divide_3_and_5(self):
        a = FizzBuzz()
        self.assertEqual(a.fizzbuzz(15), "FizzBuzz")
        self.assertEqual(a.fizzbuzz(30), "FizzBuzz")

    def test_contain_normal(self):
        a = FizzBuzz('/ or contain')
        self.assertEqual(a.fizzbuzz(1), "1")
        self.assertEqual(a.fizzbuzz(2), "2")
        self.assertEqual(a.fizzbuzz(4), "4")

    def test_contain_3(self):
        a = FizzBuzz('/ or contain')
        self.assertEqual(a.fizzbuzz(3), "Fizz")
        self.assertEqual(a.fizzbuzz(13), "Fizz")
        self.assertEqual(a.fizzbuzz(6), "Fizz")
        self.assertEqual(a.fizzbuzz(9), "Fizz")

    def test_contain_5(self):
        a = FizzBuzz('/ or contain')
        self.assertEqual(a.fizzbuzz(5), "Buzz")
        self.assertEqual(a.fizzbuzz(25), "Buzz")
        self.assertEqual(a.fizzbuzz(10), "Buzz")

    def test_contain_3_and_5(self):
        a = FizzBuzz('/ or contain')
        self.assertEqual(a.fizzbuzz(15), "FizzBuzz")
        self.assertEqual(a.fizzbuzz(35), "FizzBuzz")
        self.assertEqual(a.fizzbuzz(53), "FizzBuzz")
        self.assertEqual(a.fizzbuzz(15), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()
