# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from gilded_rose import *

filename = "print_file.txt"
f = open(filename,"w")
def printf(*args, file=f):
    return print(*args,file=f)

def print_file_content(filename=filename):
    with open(filename,"r") as f:
        print(f.read())

def test_gilded_rose_update_qulity():
    printf("OMGHAI!")
    items = [
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

    days = 2
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        printf("-------- day %s --------" % day)
        printf("name, sellIn, quality")
        for item in items:
            printf(item)
        printf("")
        GildedRose(items).update_quality()


if __name__ == "__main__":
    test_gilded_rose_update_qulity()
    # real print
    #print_file_content(filename)
