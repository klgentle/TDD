import unittest
from Args import Args


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        a = Args("l:bool,p:int,d:str", "-l true -d usr/log -p 8080")
        self.assertEqual(a.get_value("l"), True)
        self.assertEqual(a.get_value("d"), "usr/log")
        self.assertEqual(a.get_value("p"), 8080)

    def test_missing(self):
        a = Args("l:bool,p:int,d:str", "-l -d usr/log -p 8080")
        self.assertEqual(a.get_value("l"), False)

    def test_negative(self):
        a = Args("l:bool,p:int,d:str", "-l -d usr/log -p -9")
        self.assertEqual(a.get_value("p"), -9)


if __name__ == '__main__':
    unittest.main()
