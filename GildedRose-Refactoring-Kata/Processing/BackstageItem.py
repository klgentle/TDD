from Item import Item


class BackstageItem(Item):
    def __init__(self, sell_in, quality):
        self.name = "Backstage passes to a TAFKAL80ETC concert"
        self.sell_in = sell_in
        self.quality = quality

    def _is_backstage(self):
        return True
