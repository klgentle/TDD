import unittest
from Args import Args


class TestArgs(unittest.TestCase):

    def test_args(self):
        a = Args("l:bool,d:str,p:int", "-l True -d /usr/local -p 8080")
        self.assertEqual(a.get_value('l'), True)
        self.assertEqual(a.get_value('d'), "/usr/local")
        self.assertEqual(a.get_value('p'), 8080)

    def test_with_number(self):
        a = Args("l:bool,d:str,p:int", "-l -p -19 -d /usr/local")
        self.assertEqual(a.get_value('l'), False)
        self.assertEqual(a.get_value('p'), -19)
        self.assertEqual(a.get_value('d'), "/usr/local")


if __name__ == '__main__':
    unittest.main()
