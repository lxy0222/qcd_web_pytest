#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/4 10:19
# @Author : sheryl
# @Site : 
# @File : index_page.py
# @Software: PyCharm
from PageLocators.indexpage_locators import IndexPageLocator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.basepage import BasePage as BP
import random
class IndexPage(BP):
    #是否存在退出按钮
    def is_exist_logout_ele(self):
        #如果存在就返回True，不存在就返回False
        try:
            self.wait_eleVisibale(loc.login_ele,"首页-等待出现退出按钮")
            return True
        except:
            return False
    #抢投标按钮
    #-----默认第一个标
    def do_loan_by_first(self):
        self.wait_eleVisibale(loc.loan_ele,"首页-等待标按钮")
        #点击投标
        self.click_button(loc.loan_ele,"首页-点击投标按钮")
    #随机选一个标
    def do_loan_by_random(self):
        self.wait_eleVisibale(loc.loan_ele,"首页-等待标按钮")
        eles=self.get_elements(loc.loan_ele,"首页-点击投标按钮")
        #随机数
        index=random.randint(0,len(eles)-1)
        eles[index].click()