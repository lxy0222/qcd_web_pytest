import os
#获取顶级目录
project_path=os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]
#获取测试报告路径
testreport_path=project_path+r"\Common\Outputs\reportout\report.html"
#配置文件路径
config_path=project_path+r'\Common\conf\congfig.conf'
#日志输出路径
log_path=project_path+r'\Common\Outputs\logout\log.txt'
#截屏图片存放地址
screenshot_path=project_path+r'\Common\screenShot_out'
if __name__ == '__main__':
    print(project_path)
    print()
    print(log_path)
    print(screenshot_path)