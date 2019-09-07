import unittest
from Schema import Schema


class MyTestCase(unittest.TestCase):
    def test_bool(self):
        a = Schema("l:bool,p:int,d:str")
        self.assertEqual(a.get_value("l", "true"), True)
        self.assertEqual(a.get_value("l", None), False)

    def test_int(self):
        a = Schema("l:bool,p:int,d:str")
        self.assertEqual(a.get_value("p", "99"), 99)
        self.assertEqual(a.get_value("p", "-9"), -9)
        self.assertEqual(a.get_value("p", None), 8080)

    def test_str(self):
        a = Schema("l:bool,p:int,d:str")
        self.assertEqual(a.get_value("d", "usr/log"), "usr/log")

if __name__ == '__main__':
    unittest.main()
