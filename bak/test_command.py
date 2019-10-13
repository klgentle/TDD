import unittest
from bak.Command import Command


class MyTestCase(unittest.TestCase):
    def test_has_value(self):
        a = Command("-l true -d usr/local")
        self.assertEqual(a.get_value("l"), "true")
        self.assertEqual(a.get_value("d"), "usr/local")

    def test_has_no_value(self):
        a = Command("-l -d usr/local")
        self.assertEqual(a.get_value("l"), None)
        self.assertEqual(a.get_value("d"), "usr/local")

    def test_has_negative_value(self):
        a = Command("-l -p -9 -d usr/local")
        self.assertEqual(a.get_value("l"), None)
        self.assertEqual(a.get_value("p"), "-9")
        self.assertEqual(a.get_value("d"), "usr/local")


if __name__ == '__main__':
    unittest.main()

