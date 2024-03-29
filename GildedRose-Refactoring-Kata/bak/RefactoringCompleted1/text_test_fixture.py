# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *
from functools import partial
from Item import Item
from BackstageItem import BackstageItem
from AgedBrieItem import AgedBrieItem
from SulfurItem import SulfurItem
from NormalItem import NormalItem

import sys


def print_from_file(file_name: str):
    with open(file_name, "r") as f:
        file_content = f.read()
    return file_content


def BaseLineOutPut():
    items = [
        NormalItem(name="+5 Dexterity Vest", sell_in=10, quality=20),
        AgedBrieItem(sell_in=2, quality=0),
        NormalItem(name="Elixir of the Mongoose", sell_in=5, quality=7),
        SulfurItem(sell_in=0, quality=80),
        SulfurItem(sell_in=-1, quality=80),
        BackstageItem(sell_in=15, quality=20),
        BackstageItem(sell_in=10, quality=49),
        BackstageItem(sell_in=5, quality=49),
        NormalItem(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]
    f = open("print_file.txt", "w")
    printf = partial(print, file=f)

    days = 2

    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        printf("-------- day %s --------" % day)
        printf("name, sellIn, quality")
        for item in items:
            printf(item)
        printf("")
        GildedRose(items).pass_one_day()
    f.close()
    return print_from_file("print_file.txt")


if __name__ == "__main__":
    BaseLineOutPut()
