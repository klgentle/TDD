from text_test_fixture import BaseLineOutPut
import difflib

def assert_file_content_equal(baselineoutput:str, file_name2:str):
    with open(file_name2, "r") as f2:
        f2_content = f2.read()
    assert baselineoutput == f2_content
    #print(f"baselineoutput:{baselineoutput}")


if __name__ == "__main__":
    baselineoutput = BaseLineOutPut()
    assert_file_content_equal(baselineoutput, "test_fixture_result.txt")