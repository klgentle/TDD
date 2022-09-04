# -*- coding: utf-8 -*-
from __future__ import print_function

from GildedRose import *
from Item import Item
from BackstagePassItem import BackstagePassItem
from SulfurasItem import SulfurasItem
from AgedItem import AgedItem


class TestTextFixture(object):
    @staticmethod
    def get_baseline():
        baseline = ""
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            AgedItem(sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            SulfurasItem(sell_in=0, quality=80),
            SulfurasItem(sell_in=-1, quality=80),
            BackstagePassItem(sell_in=15, quality=20),
            BackstagePassItem(sell_in=10, quality=49),
            BackstagePassItem(sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]
        days = 3
        for day in range(days):
            baseline += f"-------- day {day} --------\n"
            baseline += "name, sellIn, quality\n"
            for item in items:
                baseline += str(item) + "\n"
            baseline += "\n"
            GildedRose(items).pass_one_day()
        return baseline


if __name__ == "__main__":
    baseline = TestTextFixture.get_baseline()
    print(baseline)
    print("the line number is ", len(baseline.split("\n")))
