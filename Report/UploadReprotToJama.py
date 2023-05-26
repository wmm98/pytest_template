from selenium import webdriver
import time
import os
import os.path
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# driver = webdriver.Chrome()


class Roport():
    # 打开report
    def __init__(self):

        self.driver = webdriver.Edge()

    def openReport(self, path):

        # 打开浏览器
        # 传入driver对象
        self.driver.get(path)
        self.driver.maximize_window()
        time.sleep(2)
        caselist = []
        resultlist = []
        # 总共多少个case
        caseNumber = self.driver.find_element_by_class_name("splash__title").text
        # 点击show all
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/a[2]/div').click()
        time.sleep(1)
        # 展开所有的case
        expand = self.driver.find_elements_by_class_name('angle fa fa-angle-right fa-fw fa-lg')
        expandlist = len(expand)
        expand[0].click()  # 展开TestCase
        time.sleep(1)
        for i in range(1, len(expand)):
            expand = self.driver.find_elements_by_class_name('angle fa fa-angle-right fa-fw fa-lg')
            expandlist = len(expand)
            expand[i].click()  # 展开下层的子目录
        tcs = self.driver.find_elements_by_class_name('node__name')
        for tc in range(len(tcs)):
            casename = tcs[tc].text
            if 'test_' in casename:
                tcs[tc].click()
                time.sleep(1)
                tcresult = self.driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[2]/div/div[3]/div/h2/div[1]/span').text
                # print(casename,tcresult)
                caselist.append(casename)
                resultlist.append(tcresult)
        dic = dict(zip(caselist, resultlist))
        print(dic)
        case = self.caseSum(dic)
        self.driver.close()
        return case

    # 装字典为三个类型，result={'Broken': ['Burn the system ', 'One instance check (Run in PC)'], 'Failed': ['Activate the DKM button and Alarm button with/without '], 'Passed': ['Auto flas]}
    def caseSum(self, dic):
        result = ('Broken', 'Failed', 'Passed')
        result2 = {}
        for i in range(3):
            result2.update({result[i]: []})
        for k, v in dic.items():
            if v in result2:
                result2[v].append(k)
            else:
                result2[v] = []
        print(result2)
        return result2


class Jama():
    # 打开report
    def __init__(self):
        self.driver = webdriver.Chrome()

    def clickListJs(self, no):
        self.driver.execute_script('$(arguments[0]).click()',
                                   self.driver.find_elements_by_class_name('x-combo-list-inner')[
                                       1].find_elements_by_class_name('x-combo-list-item')[no])

    def element(self, method, element):
        # 加入隐性等待
        try:
            wait = WebDriverWait(self.driver, 60)
            els = wait.until(EC.presence_of_element_located((method, element)))
            return els
        except TimeoutException as e:
            raise e

    def elementDisappear(self, method, element):
        try:
            wait = WebDriverWait(self.driver, 60)
            els = wait.until_not(EC.visibility_of_element_located((method, element)))
        except TimeoutException as e:
            raise e

    def openJama(self, path, usename, psd):
        self.driver.get(path)
        self.driver.maximize_window()
        self.element(By.ID, "j_username")
        self.driver.find_element_by_id('j_username').send_keys(usename)  # 用户名
        self.driver.find_element_by_id('j_password').send_keys(psd)  # 密码
        self.driver.find_element_by_id('loginButton').click()  # 登陆
        self.element(By.CLASS_NAME, 'x-grid3-scroller')
        # time.sleep(10)

    def selectCase(self, caselist, status, no):
        j = 0
        self.element(By.CLASS_NAME, "x-grid3-row-table")
        testcases = self.driver.find_elements_by_class_name('x-grid3-row-table')
        # print(len(testcases))
        ############################################
        ActionChains(self.driver).key_down(Keys.CONTROL).perform()  # 按下Ctrl键
        for i in range(len(testcases)):
            if j == no:
                ActionChains(self.driver).key_up(Keys.CONTROL).perform()
                break
            elif testcases[i].text.split('\n')[1] in caselist:
                testcases[i].click()
                j = j + 1
        self.batchUpdateStatus(status)

    def batchUpdateStatus(self, status):
        list = self.driver.find_elements_by_class_name('x-btn-text')  # Actions
        for i in range(len(list)):
            if list[i].text == 'Actions':
                list[i].click()
                break
        time.sleep(2)
        self.driver.find_elements_by_class_name('x-menu-item-text')[2].click()  # Batch Update Test Run Status
        time.sleep(2)
        self.element(By.CLASS_NAME, 'x-window-bwrap')  #
        if len(self.driver.find_elements_by_class_name('x-window-bwrap')) > 1:
            self.driver.find_elements_by_class_name('x-window-bwrap')[1].find_elements_by_class_name('x-btn-text')[
                2].click()  # next按钮
        else:
            self.driver.find_element_by_class_name('x-window-bwrap').find_elements_by_class_name('x-btn-text')[
                2].click()  # next按钮
        time.sleep(2)
        self.element(By.NAME, 'testRunStatus').click()
        time.sleep(2)
        if status == 'Failed':
            self.clickListJs(3)
        elif status == "Passed":
            self.clickListJs(0)
        elif status == "Broken":
            self.clickListJs(4)
        time.sleep(1)
        ################选中后点击next按钮#############################
        if len(self.driver.find_elements_by_class_name('x-window-bl')) > 1:
            self.driver.find_elements_by_class_name('x-window-bl')[1].find_elements_by_class_name(' x-btn-text')[
                1].click()
            time.sleep(2)
            ################选中后点击Commit按钮#############################
            self.driver.find_elements_by_class_name('x-window-bl')[1].find_elements_by_class_name(' x-btn-text')[
                2].click()
        else:
            self.driver.find_element_by_class_name('x-window-bl').find_elements_by_class_name(' x-btn-text')[1].click()
            time.sleep(2)
            ################选中后点击Commit按钮#############################
            self.driver.find_element_by_class_name('x-window-bl').find_elements_by_class_name(' x-btn-text')[2].click()
        self.elementDisappear(By.CLASS_NAME, 'x-window-bl')

    def closeJama(self):
        self.driver.close()


if __name__ == '__main__':
    report = Roport()
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\Report'
    actresult = report.openReport(path + '\html\index.html')
    # actresult={'Broken': ['Burn the system', 'One instance check (Run in PC)'], 'Passed': ['Upload the configuration file','Check the software function simply'], 'Failed': ['Auto flash the system']}
    brokencase = actresult['Broken']
    failedcase = actresult['Failed']
    passedcase = actresult['Passed']
    jama = Jama()
    jama.openJama('https://jama.honeywell.com/perspective.req#/testPlans/32470982/testRuns?projectId=16351440',
                  'H358193', 'HONwell123')
    jama.selectCase(brokencase, 'Broken', len(brokencase))  # 选择brokencase
    time.sleep(20)
    jama.selectCase(failedcase, 'Failed', len(failedcase))  # 选择failedcase
    time.sleep(20)
    jama.selectCase(passedcase, 'Passed', len(passedcase))  # 选择passedcase
    jama.closeJama()
