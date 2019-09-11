# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *
from functools import partial
import sys

def print_from_file(file_name:str):
    with open(file_name, "r") as f:
        file_content = f.read()
    return file_content

def BaseLineOutPut():
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
    f = open('print_file.txt','w')
    printf = partial(print, file=f)
    printf ("OMGHAI!")

    days = 2
    for day in range(days):
        printf("-------- day %s --------" % day)
        printf("name, sellIn, quality")
        for item in items:
            printf(item)
        printf("")
        GildedRose(items).update_quality()
    f.close()
    return print_from_file("print_file.txt")
    #print(print_from_file("print_file.txt"))


if __name__ == "__main__":
    BaseLineOutPut()