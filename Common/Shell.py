# -*- coding: utf-8 -*-
# @Time    : 2019/5/5
# @Author  : Zhouyangfan
# @Version : V1.0
# @File    : Shell.py

"""
封装执行shell语句方法
"""

import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o

    @staticmethod
    def kill():
        subprocess.Popen(shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).kill()
