# -*- coding: utf-8 -*-
from Item import Item


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def pass_one_day(self):
        for item in self.items:
            item.pass_one_day()
