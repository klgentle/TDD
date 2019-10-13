import unittest
from bak.Schemas import Schemas


class TestSchema(unittest.TestCase):

    def test_bool(self):
        a = Schemas("l:bool")
        self.assertEqual(a.get_value('l', "True"), True)
        self.assertEqual(a.get_value('l', "False"), False)
        self.assertEqual(a.get_value('l', None), False)

    def test_int(self):
        a = Schemas("d:int")
        self.assertEqual(a.get_value('d', "8080"), 8080)
        self.assertEqual(a.get_value('d', "-1"), -1)
        self.assertEqual(a.get_value('d', None), 8080)

    def test_str(self):
        a = Schemas("l:str")
        self.assertEqual(a.get_value('l', "Hello"), "Hello")


if __name__ == '__main__':
    unittest.main()
