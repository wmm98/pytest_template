# -*- coding: utf-8 -*-


"""
定义所有可重用的测试步骤或者方法Define all reusable test steps or methods

"""

from Conf.Config import *
import allure

import xlrd

log = Log.MyLog()
conf = Config()


class GetExcelData():

    def __init__(self):
        pass

    @allure.step("这是嵌套使用,只为了显示效果")
    def test_step(self):
        pass

    @allure.step("getXlsData--检查数据")
    def getXlsData(self, casename, excelname):

        # 只为了展示效果
        self.test_step()

        self.file = xlrd.open_workbook(conf.cases_path + r"\\" + excelname)

        self.sheet1 = self.file.sheet_by_name('case data')

        # flag 等于0的时候， 运行了EOL,不为0时运行了case
        flag = 0
        # 获取干净的test result 和 expect result
        clean_test_result = []
        clean_expect_result = []
        for i in range(1, self.sheet1.nrows):

            # print("===========================================================
            if (self.sheet1.row_values(i)[0]) != 'EOT' and (self.sheet1.row_values(i)[1]).strip() == '':
                e = "#####第 %s 行@@@@@@@@ Can not find the Case Name,please check the  colunm in excel@@@@@@@@@@@" % str(
                    i + 2)
                log.error(e)
                assert False, e
            elif (self.sheet1.row_values(i)[1]).strip() == casename.strip():

                flag += 1

                if (self.sheet1.row_values(i)[3]).strip() == "":
                    e = "##### %s : %s : test result is null, please check the data" % (
                        self.sheet1.row_values(i)[1], self.sheet1.row_values(i)[2])
                    log.error(e)
                    assert False, e
                else:
                    clean_test_result.append((self.sheet1.row_values(i)[3]).strip())
                    clean_expect_result.append((self.sheet1.row_values(i)[4]).strip())

            elif flag > 0 and (self.sheet1.row_values(i)[0]) == 'EOT':
                break  # 找到case的EOT退出循环
        return [clean_test_result, clean_expect_result, casename]
