#作者    ：YCKJ1130   

#创建时间：2020/7/7 11:08  

#文件    ：datatiemes_1.py

#编译器  ：PyCharm
class HandleTime():
    @staticmethod
    def  calculate_two_time_difference(starttime,endtime):
        dif_time=endtime-starttime
        t_str=str(dif_time)
        list_time=t_str.split(':')
        h=int(list_time[0])
        m=int(list_time[1])
        s=int(list_time[2][:2])
        comsue_time=h*3600 + m*60 + s
        return comsue_time