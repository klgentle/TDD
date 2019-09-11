# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_items_quality(self):
        for item in self.items:
            item.update_quality()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def Backstage_passes_item(self):
        return self.name == 'Backstage passes to a TAFKAL80ETC concert'

    def sulfuras_hand_of_ragnaros(self):
        return self.name == "Sulfuras, Hand of Ragnaros"

    def aged_brie(self):
        return self.name == "Aged Brie"

    def increase_quality(self):
        if self.quality < 50:
            self.quality += 1
        return self.quality 


    def update_quality(self):
            if not self.aged_brie() and not self.Backstage_passes_item():
                if self.quality > 0:
                    self.not_sulfuras_quality_decrease()
            else:
                if self.quality < 50:
                    self.quality = self.quality + 1
                    if self.Backstage_passes_item():
                        if self.sell_in < 11:
                            self.increase_quality()
                        if self.sell_in < 6:
                            self.increase_quality()

            if not self.sulfuras_hand_of_ragnaros():
                self.sell_in = self.sell_in - 1
            if self.sell_in < 0:
                if not self.aged_brie():
                    if not self.Backstage_passes_item():
                        if self.quality > 0:
                            self.not_sulfuras_quality_decrease()
                    else:
                        self.quality = self.quality - self.quality
                else:
                    self.increase_quality()

    def not_sulfuras_quality_decrease(self):
        if not self.sulfuras_hand_of_ragnaros():
            self.quality = self.quality - 1


