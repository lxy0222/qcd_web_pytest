#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/4 10:19
# @Author : sheryl
# @Site : 
# @File : login_page.py
# @Software: PyCharm
from Common.basepage import BasePage
from PageLocators.loginpage_locators import LoginPageLocator as loc
class LoginPage(BasePage):
    #登录
    def login(self,username,password,isremenber=True):
        #等待元素出现
        self.wait_eleVisibale(loc.login_xp,'登录页面')
        #输入用户名
        test=loc.phone_xp
        self.input_text(test,username,'输入用户名页面')
        #输入密码
        self.input_text(loc.pwd_xp,password,'输入密码页面')
        #勾选记住我
        if isremenber==True:
            self.get_element(loc.remember_me_checkbox,'记住我页面')
        else:
            pass
        #点击登录
        self.click_button(loc.login_xp,'点击登录')
        pass
    #进去注册
    def register_enter(self):
        #点击注册
        self.wait_eleVisibale(loc.register_but,'点击注册页面')
        self.click_button(loc.register_but,'点击注册页面')
        pass
    def forget_pwd_enter(self):
        self.click_button(loc.forget_pwd_but,'点击忘记密码')
    #获取错误提示---登录区域
    def get_errorMsg_from_login(self):
        self.wait_eleVisibale(loc.error_Msg,'获取登录提示')
        return self.driver.find_element(*loc.error_Msg).text
    #获取错误提示--正中
    def get_errorMsg_from_mid(self):
        self.wait_eleVisibale(loc.error_Msg_mid,'获取登录提示')
        return self.driver.find_element(*loc.error_Msg_mid).text