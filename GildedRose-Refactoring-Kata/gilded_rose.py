# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_items_quality(self):
        for item in self.items:
            item.update_quality()


class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def is_backstage(self):
        return self.name == "Backstage passes to a TAFKAL80ETC concert"

    def aged_brie(self):
        return self.name == "Aged Brie"

    def increase_quality(self):
        if self.quality < 50:
            self.quality += 1

    def update_quality(self):
        self.sell_in_decrease()
        if self.aged_brie():
            self.increase_quality()
            return

        if self.is_backstage():
            self.increase_quality()
            if self.sell_in < 6:
                self.increase_quality()
            return
        self.quality_decrease()

        if self.sell_in < 0:
            self.update_after_expiration()

    def sell_in_decrease(self):
        self.sell_in = self.sell_in - 1

    def update_after_expiration(self):
        self.quality_decrease()

    def quality_decrease(self):
        if self.quality > 0:
            self.quality = self.quality - 1


class Sulfuras(Item):
    def __init__(self, sell_in, quality):
        self.name = "Sulfuras, Hand of Ragnaros"
        self.sell_in = sell_in
        self.quality = quality

    def is_sulfuras(self) -> bool:
        return True

    def quality_decrease(self):
        return

    def update_sell_in_days(self):
        return

    def update_quality(self):
        return


class Backstage(Item):
    def __init__(self, sell_in, quality):
        self.name = "Backstage passes to a TAFKAL80ETC concert"
        self.sell_in = sell_in
        self.quality = quality

    def is_backstage(self) -> bool:
        return True

    def update_after_expiration(self):
        self.quality = self.quality - self.quality


class AgedBrie(Item):
    def __init__(self, sell_in, quality):
        self.name = "Aged Brie"
        self.sell_in = sell_in
        self.quality = quality

    def is_aged_brie(self) -> bool:
        return True

    def update_after_expiration(self):
        self.increase_quality()
