from text_test_fixture import *


def safety_net_test():
    # run test
    update_quality_for_days()
    with open("print_file.txt", "r") as print_file, open(
        "text_test_fixture.txt", "r"
    ) as orig_result:
        assert print_file.read() == orig_result.read()


if __name__ == "__main__":
    safety_net_test()
