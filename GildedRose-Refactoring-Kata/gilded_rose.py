# -*- coding: utf-8 -*-
import Item


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def pass_one_day(self):
        for item in self.items:
            if not item.is_aged_brie() and not item.is_backstage_passes():
                if item.quality > 0:
                    if not item.is_sulfur():
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.is_backstage_passes():
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if not item.is_sulfur():
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if not item.is_aged_brie():
                    if not item.is_backstage_passes():
                        if item.quality > 0:
                            if not item.is_sulfur():
                                item.quality = item.quality - 1
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
