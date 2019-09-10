# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *
from functools import partial

def print_from_file(file_name:str):
    with open(file_name, "r") as f:
        print(f.read())

def assert_file_content_equal(file_name1:str, file_name2:str):
    with open(file_name1, "r") as f1:
        f1_content = f1.read()
    with open(file_name2, "r") as f2:
        f2_content = f2.read()
    assert f1_content == f2_content

if __name__ == "__main__":
    f = open('print_file.txt','w')
    printf = partial(print, file=f)
    printf ("OMGHAI!")
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
    import sys
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

    # print sys.out
    #print_from_file("print_file.txt")
    assert_file_content_equal("print_file.txt", "test_fixture_result.txt")