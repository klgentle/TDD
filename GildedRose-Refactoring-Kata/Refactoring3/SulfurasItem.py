from Item import Item


class SulfurasItem(Item):

    def __init__(self, sell_in, quality):
        super().__init__(name="Sulfuras, Hand of Ragnaros", sell_in=sell_in, quality=quality)

    def is_sulf(self):
        return True

    def update_sell_in_days(self):
        return

    def update_quality_after_expiration(self):
        return

    def update_quality(self):
        return
