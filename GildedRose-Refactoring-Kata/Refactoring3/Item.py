class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def pass_one_day(self):
        self.update_sell_in_days()
        self.update_quality()
        if self.is_expired():
            self.update_quality_after_expiration()

    def update_quality(self):
        self.decrease_quality()

    def update_quality_after_expiration(self):
        self.decrease_quality()

    def decrease_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1

    def is_expired(self):
        return self.sell_in < 0

    def update_sell_in_days(self):
        self.sell_in = self.sell_in - 1

    def increase_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
