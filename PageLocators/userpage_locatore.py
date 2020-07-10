#作者    ：YCKJ1130   

#创建时间：2020/7/9 13:55  

#文件    ：userpage_locatore.py

#编译器  ：PyCharm
from selenium.webdriver.common.by import By
class UserPageLocator:
    #用户页面-可用余额标题
    charge_money_title=(By.XPATH,"//li[text()='可用余额：']")
    #用户页面-余额显示
    charge_money=(By.XPATH,"//li[@class='color_sub']")