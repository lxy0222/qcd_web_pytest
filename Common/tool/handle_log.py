#作者    ：YCKJ1130   

#创建时间：2020/7/7 15:43  

#文件    ：handle_log.py

#编译器  ：PyCharm
# 封装处理日志的类
import logging
from Common.tool.read_config import ReadConfig     # 从配置文件中获取
from Common.tool.read_path import config_path,log_path
class HandleLog:
    """
    封装处理日志的类
    """
    def __init__(self):
        # 1. 定义日志收集器
        self.case_logger = logging.getLogger(ReadConfig().read_config(config_path,"LOG","log_name"))

        # 2. 指定日志收集器的日志等级
        self.case_logger.setLevel(ReadConfig().read_config(config_path,"LOG","log_level"))

        # 3. 定义日志输出渠道
        console_handle = logging.StreamHandler()  # 定义日志输出到控制台
        file_handle = logging.FileHandler(log_path, encoding="utf-8")     # 定义日志输出到文件

        # 4. 指定日志输出渠道的日志等级
        console_handle.setLevel(ReadConfig().read_config(config_path,"LOG","console_level"))
        file_handle.setLevel(ReadConfig().read_config(config_path,"LOG","file_level"))

        # 5. 定义日志显示的格式
        simple_formatter = logging.Formatter(ReadConfig().read_config(config_path,"LOG","simple_formatter"))    # 简单点的格式
        verbose_formatter = logging.Formatter(ReadConfig().read_config(config_path,"LOG","verbose_formatter"))  # 详细的格式

        # console_handle.setFormatter(simple_formatter)   # 控制台显示简洁的日志
        file_handle.setFormatter(verbose_formatter)     # 日志文件中显示详细日志

        # 6. 对接, 将日志收集器与输出渠道对接
        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        """
        获取logger日志对象
        :return:
        """
        return self.case_logger


# do_log = HandleLog().get_logger()       # 实例化对象
    @staticmethod
    def my_loging():
        do_log = HandleLog().get_logger()
        return do_log
if __name__ == '__main__':
    do_log = HandleLog()
    case_logger = do_log.get_logger()
    case_logger.debug("这是一个debug级别的日志")  # 手动记录日志
    case_logger.info("这是一个info级别的日志")
    case_logger.warning("这是一个warning级别的日志")
    case_logger.error("这是一个error级别的日志")
    case_logger.critical("这是一个critical级别的日志")