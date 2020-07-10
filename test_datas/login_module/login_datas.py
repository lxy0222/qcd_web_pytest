#作者    ：YCKJ1130   

#创建时间：2020/7/6 9:59  

#文件    ：login_datas.py

#编译器  ：PyCharm

#正常场景--测试数据
success_data={'user':'15823887943','passwd':'test123!'}

#异常用例--手机号码格式不正确（大于11位、小于11位、为空、不在号码段）
errorphone_data=[
    {'user':'1582388794','passwd':'test123!','check':'请输入正确的手机号'},
    {'user':'158238879431','passwd':'test123!','check':'请输入正确的手机号'},
    {'user':'','passwd':'test123!','check':'请输入手机号'},
    {'user':'11823887943','passwd':'test123!','check':'请输入正确的手机号'}
]

#异常用例--手机未注册、账号或密码错误
norcgphone_or_wrongpwd=[
    {'user':'15823887943','passwd':'test123','check':'帐号或密码错误!'},
    {'user':'15823887942','passwd':'test123!','check':'此账号没有经过授权，请联系管理员!'},
]