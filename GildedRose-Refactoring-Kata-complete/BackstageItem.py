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
        self.increase_quality()
        if self.sell_in < 10:
            self.increase_quality()
        if self.sell_in < 0:
            self.increase_quality()
