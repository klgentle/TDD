import unittest
from Command import Command


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        a = Command("-l true -p 8080 -d /usr/logs")
        self.assertEqual(a.get_value('l'), "true")
        self.assertEqual(a.get_value('p'), "8080")
        self.assertEqual(a.get_value('d'), "/usr/logs")

    def test_value_missing(self):
        a = Command("-l -p 8080 -d /usr/logs")
        self.assertEqual(a.get_value('l'), None)

    def test_negative_value(self):
        a = Command("-l -p -9 -d /usr/logs")
        self.assertEqual(a.get_value('l'), None)
        self.assertEqual(a.get_value('p'), "-9")

if __name__ == '__main__':
    unittest.main()
