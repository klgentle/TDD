import unittest
from Item import Item


class TestItemUpdate(unittest.TestCase):
    def test_double_increase_backstage_pass_value_when_getting_close_to_expiration(
        self
    ):
        item = Item(
            name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=20
        )
        item.pass_one_day()
        self.assertEqual(item.quality, 21)
        item.pass_one_day()
        self.assertEqual(item.quality, 23)


if __name__ == "__main__":
    unittest.main()
