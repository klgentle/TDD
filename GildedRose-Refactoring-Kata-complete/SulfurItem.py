from Item import Item


class SulfurItem(Item):
    def __init__(self, sell_in, quality):
        self.name = "Sulfuras, Hand of Ragnaros"
        self.sell_in = sell_in
        self.quality = quality

    def _is_sulfur(self):
        return True

    def _update_sell_in(self):
        pass

    def _update_quality_after_expired(self):
        pass

    def _update_quality(self):
        pass
