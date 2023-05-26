"""

# @allure.feature # 用于定义被测试的功能，被测产品的需求点
# @allure.story # 用于定义被测功能的用户场景，即子功能点
# @allure.severity #用于定义用例优先级
# @allure.issue #用于定义问题表识，关联标识已有的问题，可为一个url链接地址
# @allure.testcase #用于用例标识，关联标识用例，可为一个url链接地址

# @allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
# @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
# allure.environment(environment=env) #用于定义environment

"""
import sys
import time
from os import path
import os


import allure
import pytest

from Conf import Config

conf = Config.Config()

path_dir = conf.path_dir


@pytest.fixture()
def fixture_with_conftest_step():
    pass


@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    # 前置文件
    allure.attach('在fixture前置操作里面添加一个附件txt', 'fixture前置附件', allure.attachment_type.TEXT)
    allure.attach('<head></head><body> 一个HTML页面 </body>', 'Attach with HTML type', allure.attachment_type.HTML)
    allure.attach.file(path_dir + '/TestCase/index.html', attachment_type=allure.attachment_type.HTML)

    # 后置文件 ,或者加 yield

    def finalizer_module_scope_fixture():
        allure.attach('在fixture后置操作里面添加一个附件txt', 'fixture后置附件',
                      allure.attachment_type.TEXT)
        allure.attach.file(path_dir + '/TestCase/index.html', attachment_type=allure.attachment_type.HTML)

    request.addfinalizer(finalizer_module_scope_fixture)

    # 添加后置文件，也可用如下方法
    # yield
    # allure.attach('在fixture后置操作里面添加一个附件txt', 'fixture后置附件',
    #               allure.attachment_type.TEXT)
    # allure.attach.file(path_dir + '/TestCase/index.html', attachment_type=allure.attachment_type.HTML)


@pytest.fixture()
def login_session():
    print("******************登录成功************************")
    yield
    print("******************退出登录**************************")
    time.sleep(2)
