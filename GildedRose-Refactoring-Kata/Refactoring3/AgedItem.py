from Item import Item


class AgedItem(Item):

    def __init__(self, sell_in, quality):
        super().__init__(name="Aged Brie", sell_in=sell_in, quality=quality)

    def is_aged(self):
        return True

    def update_quality_after_expiration(self):
        self.increase_quality()

    def update_quality(self):
        self.increase_quality()
