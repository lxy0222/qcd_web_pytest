#作者    ：YCKJ1130   

#创建时间：2020/7/9 13:51  

#文件    ：user_page.py

#编译器  ：PyCharm
from Common.basepage import BasePage
from PageLocators.userpage_locatore import UserPageLocator as loc
class UserPage(BasePage):
    def get_user_money(self):
        self.wait_eleVisibale(loc.charge_money_title,'个人页面-查看用户金额')
        return self.get_element_text(loc.charge_money,'个人页面-获取用户金额').strip("元")
