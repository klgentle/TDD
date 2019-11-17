# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from gilded_rose import *
from Item import Item
from AgedBrieItem import AgedBrieItem
from SulfurasItem import SulfurasItem
from BackstageItem import BackstageItem
from OtherItem import OtherItem


class TextTestFixture(object):
    def __init__(self):
        self.filename = "print_file.txt"
        self.items = [
            OtherItem(name="+5 Dexterity Vest", sell_in=10, quality=20),
            AgedBrieItem(sell_in=2, quality=0),
            OtherItem(name="Elixir of the Mongoose", sell_in=5, quality=7),
            SulfurasItem(sell_in=0, quality=80),
            SulfurasItem(sell_in=-1, quality=80),
            BackstageItem(sell_in=15, quality=20),
            BackstageItem(sell_in=10, quality=49),
            BackstageItem(sell_in=5, quality=49),
            OtherItem(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]

    def read_file_content(self):
        with open(self.filename, "r") as fr:
            return fr.read()

    def test_gilded_rose_update_quality(self):
        f = open(self.filename, "w")
        print("OMGHAI!", file=f)
        days = 2
        if len(sys.argv) > 1:
            days = int(sys.argv[1]) + 1
        for day in range(days):
            print("-------- day %s --------" % day, file=f)
            print("name, sellIn, quality", file=f)
            for item in self.items:
                print(item, file=f)
            print("", file=f)
            GildedRose(self.items).update_quality()


if __name__ == "__main__":
    obj = TextTestFixture()
    obj.test_gilded_rose_update_qulity()
    # real print
    # print(obj.read_file_content())
