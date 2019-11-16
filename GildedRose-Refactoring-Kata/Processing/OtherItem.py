from Item import Item


class OtherItem(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def _is_backstage(self):
        return False

    def _is_sulfuras(self):
        return False

    def _is_aged_brie(self):
        return False
