# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *
import sys

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

file_name = "print_file.txt"
f = open(file_name, "w")


def printf(*args):
    return print(*args, file=f)


def print_orig():
    with open(file_name, "r") as f:
        print(f.read())


def update_quality_for_days():
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
    f.close()


if __name__ == "__main__":
    # print ("OMGHAI!")

    update_quality_for_days()
    print_orig()
