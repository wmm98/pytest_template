import pytest


# fixture 参数化
# 字典不能单独作为fixture的传参，需要被嵌套在元组、列表中。

@pytest.fixture(params=[{"data": 888}, {"data1": 9999}], ids=['01', '02'])
def user_register(request):
    user_info = request.param
    print(f'\n==========={user_info}')
    result = 'success'
    return user_info, result


def test_ee(user_register):
    print(f'\n***********{user_register}')


# if __name__ == '__main__':
#     test_ee()
print("**************************************************************")

user_name = ['sky', 'jack']
user_pwd = ['123', '456']


@pytest.fixture(params=user_name)
def login_name(request):
    name = request.param
    return name


@pytest.fixture(params=user_pwd)
def login_pwd(request):
    pwd = request.param
    return pwd


# 多个参数化叠加是一样的效果，生成笛卡尔积
def test_login(login_name, login_pwd):
    print(login_name, login_pwd)
    print("***************类型是" + str(type(login_name)) + "**************************8")
