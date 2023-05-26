import pytest


# Scenario1
# 参数化，前面两个是变量，后面是对应的数据， 3+5--->test——input， 8---》expected
@pytest.mark.parametrize("test_input, expected", [
    ("3 + 5", 8),
    ("2 + 5", 7),
    ("7 * 5", 35),
])
def test_val(test_input, expected):
    assert eval(test_input) == expected


# Scenario2
# 多个参数化
@pytest.mark.parametrize('test_input', [1, 2, 3])
@pytest.mark.parametrize('test_output, expected', [(1, 2), (3, 4)])
# @pytest.mark.parametrize('', (3, 4))
def test_multi(test_input, test_output, expected):
    print("============================================")
    pass


# Scenario3
@pytest.mark.parametrize('inp, result', [(1, 2), (3, 4)])
def test_module(inp, result):
    assert inp + 1 == result


