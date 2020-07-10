#作者    ：YCKJ1130   

#创建时间：2020/7/6 14:53  

#文件    ：bid_page.py

#编译器  ：PyCharm

from Common.tool.handle_log import HandleLog
from PageLocators.bidpage_locators import BidPageLocator as loc
import time
from Common.basepage import BasePage as BP
class BidPage(BP):
    #投资
    def invest(self,money):
        # 输入框中输入金额
        HandleLog().get_logger().info("！！！！！！！！！开始输入投资金额！！！！！！！！！！")
        self.input_text(loc.invest_input,money,'投资-金额输入框')
        #点击投资按钮
        time.sleep(1)
        HandleLog().get_logger().info("！！！！！！！！！开始点击投标按钮！！！！！！！！！！")
        if self.get_element_text(loc.invest_btn,'投资-投标按钮')=='投标':
            self.click_button(loc.invest_btn,'投资-投标按钮')
        else:
            pass
    #获取用户金额
    def get_user_money(self):
        return self.get_element_attr(loc.invest_input,"data-amount","投资-获取用户金额页面")
        pass
    #获取投资成功提示信息
    def get_msg_from_succes_invest(self):
        time.sleep(5)
        return self.get_element_text(loc.invest_succes_msg,"投资成功提示信息页面")
    #投资成功提示框--点击查看并激活
    def click_activeButton_on_succese_popup(self):
        time.sleep(3)
        # self.wait_eleVisibale(loc.check_and_activate,"投资-等待投资成功提示框",times=50)
        self.click_button(loc.check_and_activate,"投资-点击投资成功确定按钮")
        pass
    #获取页面中间的错误信息
    def get_errorMsg_from_pagecenter(self):
        #获取文本之后关闭
        time.sleep(5)
        self.wait_eleVisibale(loc.errorMsg_text_center,"投资-等待页面中间错误信息提示")
        errorMsg=self.get_element_text(loc.errorMsg_text_center,'投资-获取页面中间错误信息提示内容')
        self.click_button(loc.errorMsg_btn_center,"投资-点击关闭页面中间错误信息提示")
        return errorMsg
        pass
    #获取提示信息-投标按钮上的
    def get_errorMsg_from_investButton(self):
        self.wait_eleVisibale(loc.invest_input,"投资-等待投资输入框存在")
        time.sleep(5)
        msg_on_btn=self.get_element_text(loc.invest_btn,"投资-获取投资输入框下按钮文本")
        return msg_on_btn
        pass