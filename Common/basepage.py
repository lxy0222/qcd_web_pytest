#作者    ：YCKJ1130   

#创建时间：2020/7/7 10:42  

#文件    ：basepage.py

#编译器  ：PyCharm
from Common.tool.handle_log import HandleLog
from Common.tool.read_path import *
import datetime
import time
from Common.tool.calculate_time import HandleTime as HT
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
class BasePage:
    '''
    BasePage类，针对PageObject类的第二次封装
    '''
    def __init__(self, driver):
        self.driver = driver
        self.my_loging=HandleLog().get_logger()

    def wait_eleVisibale(self, locator, pic_doc, times=30, poll_frequency=0.5):
        '''
        等待元素可见
        :param locator: 元素定位的XPATH元组表达式
        :param times: 最长等待时间
        :param poll_frequency: 轮询时间
        :return: None
        '''
        try:
            # 开始等待时间
            start_time = datetime.datetime.now()
            self.my_loging.info("等待元素{0}可见".format(locator))
            WebDriverWait(self.driver,times,poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            end_time = datetime.datetime.now()
            comsue_t = HT.calculate_two_time_difference(start_time, end_time)
            self.my_loging.info("等待元素{0}可见，耗时：{1}秒".format(locator, comsue_t))
        except:
            self.my_loging.exception("等待元素可见失败！！！")
            self.save_screenshot(pic_doc)
            raise

    def wait_elePresence(self,locator,pic_doc,times=30,poll_frequency=0.5):
        '''
        等待元素存在
        :param locator: 元素定位的XPATH元组表达式
        :param times: 最长等待时间
        :param poll_frequency: 轮询时间
        :return: None
        '''
        try:
            # 开始等待时间
            start_time = datetime.datetime.now()
            self.my_loging.info("等待元素{0}存在".format(locator))
            WebDriverWait(self.driver, times, poll_frequency).until(EC.presence_of_element_located(locator))
            # 结束等待时间
            end_time = datetime.datetime.now()
            comsue_t = HT.calculate_two_time_difference(start_time, end_time)
            self.my_loging.info("等待元素{0}存在，耗时：{1}秒".format(locator, comsue_t))
        except:
            self.my_loging.exception("等待元素存在失败！！！")
            self.save_screenshot(pic_doc)
            raise

    def wait_eleClickable(self, locator,pic_doc, times=30, poll_frequency=0.5):
        '''
        等待元素可点击
        :param locator: 元素定位的XPATH元组表达式
        :param times: 最长等待时间
        :param poll_frequency: 轮询时间
        :return: None
        '''
        try:
            # 开始等待时间
            start_time = datetime.datetime.now()
            self.my_loging.info("等待元素{0}可点击".format(locator))
            WebDriverWait(self.driver, times, poll_frequency).until(EC.element_to_be_clickable(locator))
            # 结束等待时间
            end_time = datetime.datetime.now()
            comsue_t = HT.calculate_two_time_difference(start_time, end_time)
            self.my_loging.info("等待元素{0}可点击，耗时：{1}秒".format(locator, comsue_t))
        except:
            self.my_loging.exception("等待元素可点击失败！！！")
            self.save_screenshot(pic_doc)
            raise
    def get_element(self,locator,pic_doc):
        '''
        查找元素操作
        :param locator: 元素定位的XPATH元组表达式
        :param pic_doc:
        :return:
        '''
        try:
            self.my_loging.info('开始查找{}元素'.format(locator))
            return self.driver.find_element(*locator)
        except:
            self.my_loging.exception("查找元素{}失败!!!".format(locator))
            self.save_screenshot(pic_doc)
            raise
    def get_elements(self,locator,pic_doc):
        '''
        查找元素操作--多个
        :param locator: 元素定位的XPATH元组表达式
        :param pic_doc:
        :return:
        '''
        try:
            self.my_loging.info('开始查找{}元素'.format(locator))
            return self.driver.find_element(*locator)
        except:
            self.my_loging.exception("查找元素{}失败!!!".format(locator))
            self.save_screenshot(pic_doc)
            raise
    def click_button(self,locator,pic_doc,timeout=20, frequency=0.5):
        '''
        点击元素操作
        :param locator: 元素定位的XPATH元组表达式
        :param pic_doc:
        :param times: 最长等待时间
        :param poll_frequency: 轮询时间
        :return: None
        '''
        try:
            self.my_loging.info("开始点击{}元素".format(locator))
            #等待元素可见
            self.wait_eleVisibale(locator,pic_doc,timeout,frequency)
            #找到元素
            ele_obj=self.get_element(locator,pic_doc)
            #进行点击
            ele_obj.click()
        except:
            self.my_loging.exception("点击{}元素失败！！！".format(locator))
            self.save_screenshot(pic_doc)
            raise
    def input_text(self,locator,text,pic_doc,timeout=20, frequency=0.5):
        '''
        输入操作
        :param locator:
        :param text：输入文本
        :param pic_doc:
        :param timeout:
        :param frequency:
        :return:
        '''
        try:
            self.my_loging.info("开始输入文本在{}元素中".format(locator))
            self.wait_eleVisibale(locator,pic_doc,timeout,frequency)
            self.get_element(locator,pic_doc).send_keys(text)   #这里引用了get_element方法，传入的locator是元素，不需要进行解包
        except:
            self.my_loging.exception("在{}元素，输入文本失败".format(locator))
            self.save_screenshot(pic_doc)
            raise
    def get_element_text(self,locator,pic_doc,timeout=20, frequency=0.5):
        '''
        获取元素对象的文本值
        :param locator:
        :param pic_doc:
        :param timeout:
        :param frequency:
        :return:
        '''
        try:
            self.my_loging.info("开始获取{}页面{}元素文本值".format(pic_doc,locator))
            self.wait_eleVisibale(locator,pic_doc,timeout, frequency)
            return self.get_element(locator,pic_doc).text
        except:
            self.my_loging.exception("获取{}页面{}元素文本值失败！！！".format(pic_doc,locator))
            self.save_screenshot(pic_doc)
            raise
    def get_element_attr(self,locator,attr_name,pic_doc,timeout=20, frequency=0.5):
        '''
        获取页面元素属性值
        :param locator:
        :param attr_name:
        :param pic_doc:
        :param timeout:
        :param frequency:
        :return:
        '''
        try:
            self.my_loging.info("开始获取{}页面{}元素的{}属性值".format(pic_doc,locator,attr_name))
            self.wait_eleVisibale(locator,pic_doc,timeout, frequency)
            return self.get_element(locator,pic_doc).get_attribute(attr_name)
        except:
            self.my_loging.info("开始获取{}页面{}元素的{}属性值失败！！！".format(pic_doc, locator, attr_name))
            self.save_screenshot(pic_doc)
            raise
    def switch_frame(self,locator,pic_doc):
        '''
        切换iframe页面
        :param locator:
        :param pic_doc:
        :param timeout:
        :param frequency:
        :return:
        '''
        try:
            self.my_loging.info("在{}中根据元素{}进行iframe切换".format(pic_doc,locator))
            self.driver.switch_to.frame(self.get_element(locator,pic_doc))
        except:
            self.my_loging.exception("在{}中根据元素{}进行iframe切换失败".format(pic_doc,locator))
            self.save_screenshot(pic_doc)
            raise

    def switch_frame_default(self,pic_doc):
        '''
        切换iframe到main页面
        :param pic_doc:
        :return:
        '''
        try:
            self.my_loging.info("切换iframe到main页面")
            self.driver.switch_to.default_context()
        except:
            self.my_loging.exception("切换iframe到main页面失败")
            self.save_screenshot(pic_doc)
            raise
    def switch_frame_parent(self,pic_doc):
        '''
        切换iframe到上一层页面
        :param pic_doc:
        :return:
        '''
        try:
            self.my_loging.info("切换iframe到上一层页面")
            self.driver.switch_to.parent_frame()
        except:
            self.my_loging.exception("切换iframe到上一层页面失败")
            self.save_screenshot(pic_doc)
            raise

    def upload_file(self, filename, pic_doc, browser_type="chrome"):
        '''
        非input标签的文件上传
        :param filename: 文件名（绝对路径）
        :param img_doc: 截图说明
        :param browser_type: 浏览器类型
        :return:
        '''
        try:
            self.my_loging.info("上传文件（{}）".format(filename))
            time.sleep(2)
            self.driver.upload(filePath=filename, browser_type=browser_type)
        except:
            self.my_loging.exception("上传文件（{}）失败！".format(filename))
            self.save_screenshot(pic_doc)
            raise
        else:
            time.sleep(2)

    def suspend_mouse(self, loc, pic_doc, timeout=20, frequency=0.5):
        '''
        鼠标悬浮
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            self.my_loging.info("在{}上根据元素<{}>进行悬浮".format(pic_doc,loc))
            self.wait_eleClickable(loc,pic_doc, timeout, frequency)
            ele = self.get_element(loc,pic_doc)
            ActionChains(self.driver).move_to_element(ele).perform()
        except:
            self.my_loging.exception("在{}上根据元素<{}>进行悬浮失败！".format(pic_doc, loc))
            self.save_screenshot(pic_doc)
            raise

    def alert_close(self,pic_doc, alert_type='alert', text=None, timeout=20, frequency=0.5):
        '''
        弹框关闭
        :param img_doc: 截图说明
        :param alert_type: 弹框类型：alert/confirm/prompt
        :param text: prompt弹框输入的文本
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            self.my_loging.info("在{}中切换并关闭{}类型的弹框".format(pic_doc, alert_type))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.alert_is_present())
            if alert_type in ['alert','confirm']:
                self.driver.switch_to.alert.accept()
            elif alert_type == 'prompt':
                self.driver.switch_to.alert.send_keys(text)
                self.driver.switch_to.alert.accept()
            else:
                self.my_loging.exception("不支持{},请确认alert的类型".format(alert_type))
        except:
            self.my_loging.exception("在{}中切换并关闭{}类型的弹框失败！".format(pic_doc, alert_type))
            self.save_screenshot(pic_doc)
            raise
        else:
            end_time = time.time()
            self.my_loging.exception("在{}中切换并关闭{}类型的弹框，等待时间：{}秒".
                             format(pic_doc,alert_type,round(end_time - start_time, 2)))

    def select_action(self, loc, pic_doc, content, select_type, timeout=20, frequency=0.5):
        '''
        Select操作
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param content: select_by_方法的入参
        :param select_type: select类型
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            self.my_loging.info("在{}上根据元素<{}>以{}方式进行下拉选择".format(pic_doc, loc, select_type))
            self.wait_eleClickable(loc,pic_doc, timeout, frequency)
            ele = self.get_element(loc,pic_doc)
            if select_type == 'index':
                self.driver.Select(ele).select_by_index(content)
            elif select_type == 'value':
                self.driver.Select(ele).select_by_value(content)
            elif select_type == 'text':
                self.driver.Select(ele).select_by_visible_text(content)
            else:
                self.my_loging.exception("不支持{},请确认Select的类型".format(select_type))
        except:
            self.my_loging.exception("在{}上根据元素<{}>以{}方式进行下拉选择失败！".format(pic_doc, loc, select_type))
            self.save_screenshot(pic_doc)
            raise
    def switch_to_windows(self, loc,pic_doc, timeout=20, frequency=0.5):
        '''
        窗口切换
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            self.my_loging.info("在{}中根据元素<{}>进行窗口切换".format(pic_doc, loc))
            cur_handles = self.driver.window_handles  # 获取点击之前的窗口总数
            start_time = time.time()
            self.click_button(loc, pic_doc, timeout, frequency)  # 点击按钮后新的窗口出现
            WebDriverWait(self.driver, timeout, frequency).until(EC.new_window_is_opened(cur_handles))
            wins = self.driver.window_handles  # 再次获取窗口总数
            self.driver.switch_to.window(wins[-1])  # 切换到新的页面
        except Exception as e:
            self.my_loging.exception("在{}中根据元素<{}>进行窗口切换失败！".format(pic_doc, loc))
            self.save_screenshot(pic_doc)
            raise e
        else:
            end_time = time.time()
            self.my_loging.info("在{}中根据元素<{}>进行窗口切换，等待时间：{}秒".
                             format(pic_doc, loc, round(end_time - start_time, 2)))
    def save_screenshot(self,pic_name):
        '''
        保存截图
        :param pic_name: 截图图片名称
        :return: None
        '''
        #图片名称：模块名_页面名称_操作名称_年-月-日_时-分-秒.png
        file_name=screenshot_path + "/{1}_{0}.png".format(
            datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H-%M-%S"),pic_name)      # 保存到那个路径，保存的名称为
        self.driver.save_screenshot(file_name)      # 存储到指定目录下
        with open(file_name, mode='rb') as f:
            file = f.read()
        self.my_loging.info("截图成功，页面截图文件保存在：{}".format(file_name))