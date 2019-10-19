class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def is_backstage_passes(self):
        return self.name == "Backstage passes to a TAFKAL80ETC concert"

    def is_aged_brie(self):
        return self.name == "Aged Brie"

    def is_sulfur(self):
        return self.name == "Sulfuras, Hand of Ragnaros"
