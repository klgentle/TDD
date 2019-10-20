class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def _is_backstage_passes(self):
        return False

    def _is_aged_brie(self):
        return False

    def _is_sulfur(self):
        return False

    def pass_one_day(self):
        self.update_sell_in()
        self.update_quality()
        if self.is_expired():
            self.update_quality_after_expired()

    def update_quality(self):
        if not self._is_aged_brie() and not self._is_backstage_passes():
            if self.quality > 0:
                if not self._is_sulfur():
                    self.quality = self.quality - 1
        else:
            if self.quality < 50:
                self.quality = self.quality + 1
                if self._is_backstage_passes():
                    if self.sell_in < 10:
                        if self.quality < 50:
                            self.quality = self.quality + 1
                    if self.sell_in < 0:
                        if self.quality < 50:
                            self.quality = self.quality + 1

    def update_quality_after_expired(self):
        if not self._is_aged_brie():
            if not self._is_backstage_passes():
                if self.quality > 0:
                    if not self._is_sulfur():
                        self.quality = self.quality - 1
            else:
                self.quality = 0
        else:
            if self.quality < 50:
                self.quality = self.quality + 1

    def is_expired(self):
        return self.sell_in < 0

    def update_sell_in(self):
        if not self._is_sulfur():
            self.sell_in = self.sell_in - 1
