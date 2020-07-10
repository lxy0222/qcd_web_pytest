#作者    ：YCKJ1130   

#创建时间：2020/7/6 14:14  

#文件    ：test_loan.py

#编译器  ：PyCharm

import pytest
import allure
from PageObject.bid_page import BidPage as BP
from test_datas.invest_module.invest_datas import *
from Common.tool.handle_log import HandleLog
from PageObject.user_page import UserPage as UP
@pytest.mark.usefixtures('login_web')
@pytest.mark.usefixtures('refresh_page')
@pytest.mark.usefixtures('select_bid')
@allure.feature('投资模块')
class TestInvest:
    '''
    投资测试
    '''
    @allure.story("投资失败投标置灰-非100整数倍")
    @pytest.mark.parametrize('datas',no100_money)
    def test_invest_failed_no100(self,datas,login_web):
        '''
        投资失败投标置灰  非100整数倍且大于100，非100整数倍且小于100，字母，符号
        :param datas:测试数据集
        :param login_web: 返回的driver对象
        :return:
        '''
        HandleLog().get_logger().info("===========================投资用例：异常场景-非100整倍================================")
        userMoney_investBefore = BP(login_web).get_user_money()  # 投资前用户金额
        BP(login_web).invest(datas['money'])   #用户投资
        Msg=BP(login_web).get_errorMsg_from_pagecenter()        #获取页面中央弹窗信息提示内容
        userMoney_investAfter = BP(login_web).get_user_money()  # 投资后用户金额
        try:
            assert datas['check'] == Msg   #断言提示信息内容
            assert userMoney_investBefore==userMoney_investAfter    #操作前后金额不边
            HandleLog().get_logger().info("投资异常用例-非100整数倍，断言通过")
        except:
            HandleLog().get_logger().exception("投资异常用例-非100整数倍，断言失败！")

    @allure.story("投资失败弹框提示-非10整数倍")
    @pytest.mark.parametrize('datas', no10_money)
    def test_invest_failed_no10(self,datas,login_web):
        '''
        投资失败弹框提示  负数100整数倍金额，0，空格，100整数倍且小于100,投标的金额大于标剩余金额，购买标的金额大于标总金额，投标金额大于可用金额
        :param datas:测试数据集
        :param login_web:返回的driver对象
        :return:
        '''
        HandleLog().get_logger().info("===========================投资用例：异常场景-非10整数倍================================")
        userMoney_investBefore = BP(login_web).get_user_money()  # 投资前用户金额
        BP(login_web).invest(datas['money'])
        Msg=BP(login_web).get_errorMsg_from_investButton()
        login_web.refresh()            #刷新页面
        userMoney_investAfter = BP(login_web).get_user_money()  # 投资后用户金额
        try:
            assert datas['check']==Msg
            assert userMoney_investAfter==userMoney_investBefore
            HandleLog().get_logger().exception("投资异常用例-非10整数倍，断言通过")
        except:
            HandleLog().get_logger().exception("投资异常用例-非10整数倍，断言失败！")

    @allure.story("投资成功")
    def test_invest_success(self,login_web):
        '''
        投资金额正常
        :param login_web:返回的driver对象
        :return:
        '''
        HandleLog().get_logger().info("===========================投资用例：正常场景-投资成功================================")
        userMoney_investBefore = BP(login_web).get_user_money()  # 投资前用户金额
        BP(login_web).invest(success_money['money'])
        BP(login_web).click_activeButton_on_succese_popup()
        # 验证
        # 个人页面---获取用户当前余额
        userMoney_investAfter = UP(login_web).get_user_money()
        try:
            assert success_money['money'] == str(int(float(userMoney_investBefore) - float(userMoney_investAfter)))
            HandleLog().get_logger().exception("投资正常用例断言通过")
        except:
            HandleLog().get_logger().exception("投资正常用例断言失败！")

if __name__ == '__main__':
    a='9650900.00'
    b='9650800.00'
    print(int(float(a)-float(b)))