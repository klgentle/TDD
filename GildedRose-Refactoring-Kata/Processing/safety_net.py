# gilded_rose_safety_net
from text_test_fixture import TextTestFixture
from difflib import Differ
from pprint import pprint


def test_result():
    # 运行测试
    obj = TextTestFixture()
    obj.test_gilded_rose_update_qulity()

    # compare result
    with open("original_result.txt", "r") as orig_result:
        assert orig_result.read() == obj.read_file_content()
        # d = Differ()
        # pprint(list(d.compare(orig_result.read(), obj.read_file_content())))


if __name__ == "__main__":
    test_result()
