# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.not_aged_brie() and not item.Backstage_passes_item():
                if item.quality > 0:
                    if item.not_sulfuras_hand_of_ragnaros():
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.Backstage_passes_item():
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.not_sulfuras_hand_of_ragnaros():
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.not_aged_brie():
                    if not item.Backstage_passes_item():
                        if item.quality > 0:
                            if item.not_sulfuras_hand_of_ragnaros():
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def Backstage_passes_item(self):
        return self.name == 'Backstage passes to a TAFKAL80ETC concert'

    def not_sulfuras_hand_of_ragnaros(self):
        return self.name != "Sulfuras, Hand of Ragnaros"

    def not_aged_brie(self):
        return self.name != "Aged Brie"