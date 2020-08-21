import random
# wheat_list =['adsad',454,"哈哈哈"]
# for i,j in enumerate(wheat_list) :
#     print(i,j)
import time
import datetime


t=datetime.datetime.now()

t1=(t+datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
ts1=time.mktime(time.strptime(t1, '%Y-%m-%d %H:%M:%S'))
print(int(ts1))

t=datetime.datetime.now()

#当前日期
t3 =t.strftime('%Y-%m-%d %H:%M:%S')
#转为秒级时间戳
ts3=time.mktime(time.strptime(t3, '%Y-%m-%d %H:%M:%S'))
print(ts3)