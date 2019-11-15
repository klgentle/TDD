# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from gilded_rose import *


class TextTestFixture(object):
    def __init__(self):
        self.filename = "print_file.txt"
        self.f = open(self.filename,"w")
        self.items = [
                 Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
                 Item(name="Aged Brie", sell_in=2, quality=0),
                 Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
                 Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                 Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                 Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
                 Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
                 Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
                 Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
                ]

    def printf(self, *args):
        return print(*args,file=self.f)
    
    def read_file_content(self):
        with open(self.filename,"r") as f:
            return f.read()
    
    def test_gilded_rose_update_qulity(self):
        self.printf("OMGHAI!")
        days = 2
        if len(sys.argv) > 1:
            days = int(sys.argv[1]) + 1
        for day in range(days):
            self.printf("-------- day %s --------" % day)
            self.printf("name, sellIn, quality")
            for item in self.items:
                self.printf(item)
            self.printf("")
            GildedRose(self.items).update_quality()


if __name__ == "__main__":
    obj = TextTestFixture()
    obj.test_gilded_rose_update_qulity()
    # real print
    #print(read_file_content())
