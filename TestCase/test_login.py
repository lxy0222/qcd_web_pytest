#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/4 10:56
# @Author : sheryl
# @Site : 
# @File : test_login.py
# @Software: PyCharm

import pytest
import allure
from test_datas.login_module.login_datas import *
from PageObject.index_page import IndexPage as ID
from PageObject.login_page import LoginPage as LG
from Common.tool.handle_log import HandleLog
@pytest.mark.usefixtures('access_web')
@pytest.mark.usefixtures('refresh_page')
@allure.description("测试登录用例，采用正向和反向场景对账号密码组合验证")
@allure.feature("登录模块")
@pytest.mark.login
class TestLogin:
    @allure.story("手机号码格式不正确")
    @allure.severity('critical')
    @allure.step("测试手机号格式错误场景用例")
    @pytest.mark.parametrize('data',errorphone_data)
    def test_login_error_phone(self,data,access_web):
        '''
        手机号格式错误（大于11位、小于11位、为空、不在号码段）
        :param data: 测试用例集
        :param access_web: driver实例化
        :return:
        '''
        with allure.step("1：输入用户名{}；2：输入密码{}；3：点击登录".format(data['user'],data['passwd'])):
            LG(access_web).login(data['user'],data['passwd'])
        #断言 提示请输入正确的手机号
        #登录页面中获取提示框的文本内容
        #比对文本内容与预期值是否相等
        try:
            assert LG(access_web).get_errorMsg_from_login()==data['check']
        except:
            HandleLog().get_logger().exception("断言失败！！！")
            raise

    @allure.step("测试手机号未注册及密码错误场景用例")
    @allure.story("手机号码未注册、错误密码")
    @pytest.mark.parametrize('data',norcgphone_or_wrongpwd)
    def test_login_0_norcgphone_or_wrongpwd(self,data,access_web):
        '''
        未注册手机号、错误密码
        :param data: 测试用例集
        :param access_web: driver实例化
        :return:
        '''
        LG(access_web).login(data['user'],data['passwd'])
        try:
            assert LG(access_web).get_errorMsg_from_mid()==data['check']
        except:
            HandleLog().get_logger().exception("断言失败！！！")
            raise
    #用例正常登录
    @allure.step("测试正常登陆用例场景")
    @allure.story("正常登陆测试")
    def test_login_1_seccess(self,access_web):
        '''
        正常登录用例
        :param access_web: driver实例化
        :return:
        '''
        LG(access_web).login(success_data['user'],success_data['passwd'],isremenber=False)
        #断言
        try:
            assert ID(access_web).is_exist_logout_ele()
        except:
            HandleLog().get_logger().exception("断言失败！！！")
            raise