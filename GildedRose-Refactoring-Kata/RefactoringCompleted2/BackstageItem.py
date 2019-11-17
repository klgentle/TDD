from Item import Item


class BackstageItem(Item):
    def __init__(self, sell_in, quality):
        self.name = "Backstage passes to a TAFKAL80ETC concert"
        self.sell_in = sell_in
        self.quality = quality

    def _is_backstage(self):
        return True

    def _update_quality(self):
        self._quality_increase()
        if self.sell_in < 10:
            self._quality_increase()
        if self.sell_in < 5:
            self._quality_increase()

    def _update_quality_after_expiration(self):
        self.quality = self.quality - self.quality
