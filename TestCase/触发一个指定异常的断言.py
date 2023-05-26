import pytest


# Scenario1
def f():
    # 解析器请求退出
    raise SystemExit(1)


def test_mytest():
    # 当调用f()时出现SystemExit异常，则表示程序是正确的，出现其他异常表明程序是错误的
    with pytest.raises(SystemExit):
        f()


# Scenario2
def myfunc():
    # 引起值错误
    raise ValueError("返回40013支付错误")


def test_match():
    # 当调用myfunc()时出现值错误。则表示程序是正确的
    # 将值的信息保存到excinfo中，并且可能断言值中的属性value的内容
    with pytest.raises(ValueError) as excinfo:
        myfunc()
    print("没有执行到这里")
    assert '40013' in str(excinfo)


# Scenario3
# 异常类型可以写多个，后面可以跟正则表达式，与断言类似
def test_match_assertError():
    with pytest.raises((ValueError, RuntimeError), match=r".*40013"):
        myfunc()
