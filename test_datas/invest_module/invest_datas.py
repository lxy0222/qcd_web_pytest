#作者    ：YCKJ1130   

#创建时间：2020/7/6 16:51  

#文件    ：invest_datas.py

#编译器  ：PyCharm

#投资金额
#正常投资
success_money={'money':'100','check':'投标成功！'}
# 投标按钮错误提示
no10_money=[
    {'money':'1','check':'请输入10的整数倍'},
    {'money':'101','check':'请输入10的整数倍'},
    {'money':'english','check':'请输入10的整数倍'},
    {'money':'中文','check':'请输入10的整数倍'},
    {'money':'@@','check':'请输入10的整数倍'}
              ]
no100_money=[
    {'money':'10','check':'投标金额必须为100的倍数'},
    {'money':' ','check':'请正确填写投标金额'},
    {'money':'-10','check':'请正确填写投标金额'},
    {'money':'110','check':'投标金额必须为100的倍数'}
              ]