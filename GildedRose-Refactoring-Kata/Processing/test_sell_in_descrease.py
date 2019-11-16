from Item import Item


def test_sell_in_descrease():
    # 测试临界值 11， 6
    item = Item(
        name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=20
    )
    item.pass_one_day()
    assert item.quality == 21
    item.pass_one_day()
    assert item.quality == 23


if __name__ == "__main__":
    test_sell_in_descrease()
