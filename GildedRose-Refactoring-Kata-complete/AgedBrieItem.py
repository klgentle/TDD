from Item import Item


class AgedBrieItem(Item):
    def __init__(self, sell_in, quality):
        self.name = "Aged Brie"
        self.sell_in = sell_in
        self.quality = quality

    def _is_aged_brie(self):
        return True

    def _update_quality_after_expired(self):
        self.increase_quality()

    def _update_quality(self):
        self.increase_quality()
