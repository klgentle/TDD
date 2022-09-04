from TestTextFixture import TestTextFixture


class TestGildedRoseSafetyNet(object):
    @staticmethod
    def should_always_align_with_baseline():
        output = TestTextFixture.get_baseline()
        baseline = ""
        with open("baseline.txt", "r") as f:
            baseline = f.read()
        assert output == baseline


if __name__ == "__main__":
    TestGildedRoseSafetyNet.should_always_align_with_baseline()