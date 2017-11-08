# python对象
# 括号里的object代表这个类从object继承 如果有别的类继承也可以
# __init__初始化函数 参数中self是代表当前类的实例 也就相当于进行绑定 这个是python自己会绑定当前实例到self上的的 所以我们传入参数 不需要传self
#
# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def print_score(self):
#         print('%s: %s' % (self.name,self.score))
# one = Student('shp',99)
# two = Student('shp2',102)
# one.print_score()
# two.print_score()
# print(one.name)

# 实例变量访问
# 正常的变量可以被外部访问，变成私有变量有利于数据的安全 利用双下划线__score
# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name
#         self.score = score
#     def print_score(self):
#         print('%s: %s' % (self.__name,self.score))
# one = Student('shp',99)
# two = Student('shp2',102)
# print(one.__name)

# 如果要是访问私有变量 那么可以使用setget等函数
# 其实 python访问不了__name变量是因为python给进行了一步转换 _Student__name 通过这个还是可以访问的
# 所以都是靠自觉了 按照规范来

# 静态语言与动态语言
# 静态语言比如java继承多态是必须要按照同一父级的
# 但是对于python这种动态语言而言 只要传入的对象有一样的方法就可以

# 获取对象信息 type() 返回对应的class类型
# print(type('sss'))
# 判断是否是函数 使用types去判断
# import types
# def fn():
#     pass
# print(type(fn))
# 判断是否是一个具体的类型 isinstance(xxx,type)
# print(isinstance('sss',str))
# 判断是否符合某些类型
# print(isinstance([1,2,3,4],(tuple,list)))
# 获取对象的所有属性和方法
print(dir('sss'))
# getattr 获取属性 setattr 设置属性 hasattr是否有这个属性
