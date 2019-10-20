from Item import Item


class SulfurItem(Item):
    def __init__(self, sell_in, quality):
        self.name = "Sulfuras, Hand of Ragnaros"
        self.sell_in = sell_in
        self.quality = quality

    def _is_sulfur(self):
        return True
