#作者    ：YCKJ1130   

#创建时间：2020/7/9 11:00  

#文件    ：conftest.py

#编译器  ：PyCharm
import pytest
from PageObject.index_page import IndexPage as ID
@pytest.fixture(scope='class')
def select_bid(login_web):
    ID(login_web).do_loan_by_first()   #选择第一个标
    yield login_web