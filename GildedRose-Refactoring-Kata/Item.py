class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def pass_one_day(self):
        self._update_sell_in()
        self._update_quality()
        if self.is_expired():
            self._update_quality_after_expired()

    def _update_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1

    def _update_quality_after_expired(self):
        if self.quality > 0:
            self.quality = self.quality - 1

    def is_expired(self):
        return self.sell_in < 0

    def _update_sell_in(self):
        self.sell_in = self.sell_in - 1
