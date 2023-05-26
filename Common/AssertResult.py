import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Common.Log import *
from Conf.Config import *
import allure

log = MyLog()


# 断言判断类
class AssertOutput():

    def __init__(self):
        pass

    """
             判断结果是否与text一致
             :return:True or False
        """
    @allure.step("assertText--验证结果")
    def assertText(self, check_result):

        clean_test_result = check_result[0]
        clean_expect_result = check_result[1]
        casse_name = check_result[2]
        # 列表长度：
        len_data = len(clean_expect_result)
        flag = 0
        for i in range(len_data):
            if clean_test_result[i] in clean_expect_result[i]:
                flag += 1
            else:
                log.error("##### %s test result is not equal to expect result， pls check the data#################" % (
                    casse_name))

        # flag的大小等于列表长度，则返回Ture, 否则返回false
        if flag == len_data:
            log.info("######### %s pass #################" % casse_name)
            return True
        else:
            log.error("######### %s fail #################" % casse_name)
            assert False, "######### %s fail #################" % casse_name
