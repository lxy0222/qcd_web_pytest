#作者    ：YCKJ1130   

#创建时间：2020/7/8 14:35  

#文件    ：conftest.py

#编译器  ：PyCharm
from selenium import webdriver
from test_datas.common_datas import *
from PageObject.login_page import LoginPage
import pytest
@pytest.fixture(scope='class')
def access_web():
    #前置-打开一个浏览器
    print("==============所有用例之前的，setup=======整个测试类只执行一次=================")
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    yield driver
    #后置操作
    print("==============所有用例之后的，setup=======整个测试类只执行一次=================")
    driver.quit()

@pytest.fixture(scope='class')
def login_web(access_web):
    LoginPage(access_web).login(user,pwd)
    yield access_web
    print("=================每个用例的后置========================================")

@pytest.fixture(scope='function')
def refresh_page(access_web):
    yield access_web
    access_web.refresh()
