#作者    ：YCKJ1130   

#创建时间：2020/7/6 13:57  

#文件    ：indexpage_locator.py

#编译器  ：PyCharm

from selenium.webdriver.common.by import By
class IndexPageLocator:
    #首页 退出按钮
    login_ele =(By.XPATH,"//a[contains(text(),'退出')]")
    #首页-第一个抢投标按钮
    loan_ele =(By.XPATH, "//a[contains(text(),'抢投标')]")