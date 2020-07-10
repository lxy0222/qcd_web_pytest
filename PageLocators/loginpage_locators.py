#作者    ：YCKJ1130   

#创建时间：2020/7/6 10:54  

#文件    ：loginpage_locators.py

#编译器  ：PyCharm

from selenium.webdriver.common.by import By
class LoginPageLocator:
    #---------登录页面----------#
    #手机号输入框
    phone_xp = (By.XPATH,"//input[@name='phone']")
    #密码输入框
    pwd_xp = (By.XPATH,"//input[@name='password']")
    #登录按钮
    login_xp =(By.XPATH,"//button[text()='登录']")
    #免费注册按钮
    register_but =(By.XPATH,"//a[contains(text(),'免费注册')]")
    #登录区域错误提示
    error_Msg =(By.XPATH,"//div[@class='form-error-info']")
    #获取登录错误提示--正中
    error_Msg_mid =(By.XPATH,"//div[@class='layui-layer-content']")
    #记住手机号勾选框
    remember_me_checkbox=(By.XPATH,"//input[@name='remember_me']")
    #忘记密码按钮
    forget_pwd_but=(By.XPATH,"//a[contains(text(),'忘记密码?')]")