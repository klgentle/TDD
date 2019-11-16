class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def is_backstage(self):
        return self.name == "Backstage passes to a TAFKAL80ETC concert"

    def is_sulfuras(self):
        return self.name == "Sulfuras, Hand of Ragnaros"

    def is_aged_brie(self):
        return self.name == "Aged Brie"

    def pass_one_day(self):
        self.sell_in_decrease()
        self.update_quality()
        self.update_quality_after_expiration()

    def update_quality(self):
        if not self.is_aged_brie() and not self.is_backstage():
            if self.quality > 0:
                if not self.is_sulfuras():
                    self.quality = self.quality - 1
        else:
            if self.quality < 50:
                self.quality = self.quality + 1
                if self.is_backstage():
                    if self.sell_in < 10:
                        if self.quality < 50:
                            self.quality = self.quality + 1
                    if self.sell_in < 5:
                        if self.quality < 50:
                            self.quality = self.quality + 1

    def sell_in_decrease(self):
        if not self.is_sulfuras():
            self.sell_in = self.sell_in - 1

    def update_quality_after_expiration(self):
        if self.sell_in < 0:
            if not self.is_aged_brie():
                if not self.is_backstage():
                    if self.quality > 0:
                        if not self.is_sulfuras():
                            self.quality = self.quality - 1
                else:
                    self.quality = self.quality - self.quality
            else:
                if self.quality < 50:
                    self.quality = self.quality + 1
