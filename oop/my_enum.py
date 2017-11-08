# 枚举类
from enum import Enum,unique

# Month = Enum('Month',('Jan','Feb'))

# 可以遍历枚举
# for name,member in Month.__members__.items():
#     print('name',name,'value',member.value)
# 可以看出默认值从1开始
# 我们可以自己设值 unique代表会检查是否有重复的值
@unique
class WeekDay(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Web = 3
    Thu = 4
    Fri = 5
    Sat = 6
# 访问的方式
print(WeekDay.Mon)
print(WeekDay.Mon.value)
print(WeekDay['Mon'])
print(WeekDay(5))