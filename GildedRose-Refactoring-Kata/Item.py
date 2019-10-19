class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def is_backstage_passes(self):
        return self.name == "Backstage passes to a TAFKAL80ETC concert"

    def is_aged_brie(self):
        return self.name == "Aged Brie"

    def is_sulfur(self):
        return self.name == "Sulfuras, Hand of Ragnaros"

    def pass_one_day(self):
        self.update_sell_in()
        self.update_quality()
        if self.is_expired():
            self.update_quality_after_expired()

    def update_quality(self):
        if not self.is_aged_brie() and not self.is_backstage_passes():
            if self.quality > 0:
                if not self.is_sulfur():
                    self.quality = self.quality - 1
        else:
            if self.quality < 50:
                self.quality = self.quality + 1
                if self.is_backstage_passes():
                    if self.sell_in < 10:
                        if self.quality < 50:
                            self.quality = self.quality + 1
                    if self.sell_in < 0:
                        if self.quality < 50:
                            self.quality = self.quality + 1

    def update_quality_after_expired(self):
        if not self.is_aged_brie():
            if not self.is_backstage_passes():
                if self.quality > 0:
                    if not self.is_sulfur():
                        self.quality = self.quality - 1
            else:
                self.quality = 0
        else:
            if self.quality < 50:
                self.quality = self.quality + 1

    def is_expired(self):
        return self.sell_in < 0

    def update_sell_in(self):
        if not self.is_sulfur():
            self.sell_in = self.sell_in - 1


class BackstageItem(Item):
    def __init__(self, sell_in, quality):
        self.name = "Backstage passes to a TAFKAL80ETC concert"
        self.sell_in = sell_in
        self.quality = quality


class AgedBrieItem(Item):
    def __init__(self, sell_in, quality):
        self.name = "Aged Brie"
        self.sell_in = sell_in
        self.quality = quality


class SulfurItem(Item):
    def __init__(self, sell_in, quality):
        self.name = "Sulfuras, Hand of Ragnaros"
        self.sell_in = sell_in
        self.quality = quality

class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name 
        self.sell_in = sell_in
        self.quality = quality