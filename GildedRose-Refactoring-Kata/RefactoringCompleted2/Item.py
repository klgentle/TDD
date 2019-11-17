class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def _quality_decrease(self):
        if self.quality > 0:
            self.quality = self.quality - 1

    def _quality_increase(self):
        if self.quality < 50:
            self.quality = self.quality + 1

    def pass_one_day(self):
        self.sell_in_decrease()
        self._update_quality()
        if self.sell_in < 0:
            self._update_quality_after_expiration()

    def sell_in_decrease(self):
        self.sell_in = self.sell_in - 1

    def _update_quality(self):
        self._quality_decrease()

    def _update_quality_after_expiration(self):
        self._quality_decrease()
