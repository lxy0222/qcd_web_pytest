#作者    ：YCKJ1130   

#创建时间：2020/7/6 15:34  

#文件    ：bidpage_locators.py

#编译器  ：PyCharm
from selenium.webdriver.common.by import By
class BidPageLocator:
    #投资金额输入框
    invest_input=(By.XPATH,"//input[@class='form-control invest-unit-investinput']")
    #投标按钮
    invest_btn=(By.XPATH,"//button[@class='btn btn-special height_style']")
    #投资成功文本提示
    invest_succes_msg=(By.XPATH,"//div[text()='投标成功！']")
    #投资成功后-查看并激活按钮
    check_and_activate=(By.XPATH,"//div[@class='layui-layer-content']//child::button[text()='查看并激活']")
    #中间页面错误提示文本
    errorMsg_text_center=(By.XPATH,"//div[@class ='text-center']")
    #中间页面错误提示关闭按钮---确定
    errorMsg_btn_center=(By.XPATH,"//a[@class='layui-layer-btn0']")

