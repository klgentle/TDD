# -*- coding: utf-8 -*-
import unittest

from Item import Item
from BackstagePassItem import BackstagePassItem


class ItemTest(unittest.TestCase):
    def test_double_increase_backstage_pass_value(self):
        item = BackstagePassItem(sell_in=11, quality=20)
        item.pass_one_day()
        self.assertEquals(item.quality, 21)
        item.pass_one_day()
        self.assertEquals(item.quality, 23)


if __name__ == '__main__':
    unittest.main()
