from Item import Item


class BackstagePassItem(Item):

    def __init__(self, sell_in, quality):
        super().__init__(name="Backstage passes to a TAFKAL80ETC concert", sell_in=sell_in, quality=quality)

    def is_backstage_pass(self):
        return True

    def update_quality_after_expiration(self):
        self.quality = 0

    def update_quality(self):
        self.increase_quality()

        if self.sell_in < 10:
            self.increase_quality()
        if self.sell_in < 5:
            self.increase_quality()
