from Item import Item


class BackstageItem(Item):
    def __init__(self, sell_in, quality):
        self.name = "Backstage passes to a TAFKAL80ETC concert"
        self.sell_in = sell_in
        self.quality = quality

    def _is_backstage_passes(self):
        return True

    def _update_quality_after_expired(self):
        self.quality = 0

    def _update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 10:
                if self.quality < 50:
                    self.quality = self.quality + 1
            if self.sell_in < 0:
                if self.quality < 50:
                    self.quality = self.quality + 1
