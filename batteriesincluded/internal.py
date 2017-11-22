# 内置模块
# 时间
# 时间模块 datetime
# 导入时间类 datetime
# from datetime import datetime
# 获取当前时间
# now = datetime.now()
# print(now)

# 设置一个时间
# dt = datetime(2017,6,30,12,14,30)
# print(dt)

# 转换为时间戳
# print(dt.timestamp())


# 从时间戳转换为datetime时间对象 是本地时间也就是北京时间 时区为utc+8:00
# dtimestamp = 1429417200.0
# print(datetime.fromtimestamp(dtimestamp))

# utc时间 utc时间是带时区的默认是标准时区
# print(datetime.utcfromtimestamp(dtimestamp))

# str转换为datetime对象
# cday = datetime.strptime('2017-04-20 18:16:30','%Y-%m-%d %H:%M:%S')
# print(cday)

# 同样的可以把datetime转换为字符串
# dstr = now.strftime('%Y-%m-%d %H:%M:%S')
# print(dstr)

# 对时间的加减
# from datetime import datetime,timedelta
# 对时间的增减需要导入timedelta 通过加减timedelta对象来实现
# 加10个小时 也就是对应的年月日等等都可以加减
# now = datetime.now()
# addtenh = now + timedelta(hours=10,)
# print(addtenh)

# 时区
# 需要导入timezone 可以对时间进行时区的转换
from datetime import datetime,timedelta,timezone
# 设置时区为utc +8
tz_zh = timezone(timedelta(hours=8))
now = datetime.now()
print(now)

# 设置时区
dt = now.replace(tzinfo=tz_zh)
print(dt)
