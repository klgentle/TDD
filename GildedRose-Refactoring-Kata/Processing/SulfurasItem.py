from Item import Item


class SulfurasItem(Item):
    def __init__(self, sell_in, quality):
        self.name = "Sulfuras, Hand of Ragnaros"
        self.sell_in = sell_in
        self.quality = quality

    def _is_sulfuras(self):
        return True
