"""
运行用例集：
    python3 run.py

# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'

"""
import sys
from Common.Email import *
import pytest
from selenium import webdriver
from Common import Log
from Common import Shell
import subprocess
from Conf import Config
import os
import os.path
import time
import shutil
import datetime
from Common.Email import *

if __name__ == '__main__':

    # 初始化
    conf = Config.Config()
    log = Log.MyLog()
    SendEmail = Email()
    shell = Shell.Shell()

    log.info('initialize Config, path=' + conf.conf_path)

    # 获取报告地址
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 清空XML文件夹然后重创文件夹
    # if os.path.exists(xml_report_path):
    #     shutil.rmtree(xml_report_path)
    #
    # os.mkdir(xml_report_path)
    #
    # cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    # try:
    #     shell.invoke(cmd)
    # except Exception:
    #     log.error('Failed to execute case, check environment configuration!!')
    #     raise

    env_path = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))) + '\pytest_debug\Report\environment.properties'
    shutil.copy(env_path, xml_report_path)

    # # 定义测试集
    allure_list = '--allure-features=pytest_debug'
    allure_story = '--allure-stories=pytest_debug_story'
    # pytest -s --allure-features pytest_debug
    # pytest -s --allure-features pytest_debug --allure-stories pytest_debug_story

    # 运行选中的case
    args = ['-s', '-q', '--alluredir', xml_report_path, allure_list, allure_story]

    # 如下参数不添加allure_list，会自动运行项目里面带有feature侦听器的的所有case
    # args = ['-s', '-q', '--alluredir', xml_report_path]
    log.info('Execution Testcases List：%s' % allure_list)
    curr_time = datetime.datetime.now()
    # print(curr_time)
    log.info('Execution Testcases start time: %s' % curr_time)
    pytest.main(args)
    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    # 复制后的项目可手动清除或生成
    # allure generate xml -o html --clean

    try:
        shell.invoke(cmd)
        # print(cmd)
    except Exception:
        log.error('Failed to execute case, check environment configuration!!')
        raise

    # allure生成报表，并启动程序
    # subprocess.call(cmd, shell=True)
    # subprocess.call('allure open -h 127.0.0.1 -p 9999 ./report/html', shell=True)

    # 打开报告
    end_time = datetime.datetime.now()
    print(end_time)
    testpreiod = end_time - curr_time
    print(testpreiod)
    log.info('Execution Testcases End time: %s' % end_time)
    log.info('Execution Testcases total time: %s' % testpreiod)

    # 生成报告，发送测试数据和报告
    # attachment_path = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    # lasteamil_path = attachment_path + '/pytest_debug/index.html'  # 此函数用于获取最新邮件附件的路径，例如#F:/email\20220210144217
    # # \异常通知.xlsx
    # lasteamil_path2 = attachment_path + '/pytest_debug/testDemo.xlsx'
    # if lasteamil_path:
    #     content = '异常数据如附件所示'
    #     tolist = ['792545884@qq.com', '920691848@qq.com']  # 收件人邮箱
    #     subject = '政通传媒异常数据通知'
    #     SendEmail.sendeamil(tolist, subject, content, lasteamil_path, lasteamil_path2)
