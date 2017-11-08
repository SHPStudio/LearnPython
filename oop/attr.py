# 实例的属性和类的属性
# 实例的属性是通过__init__绑定或者运行时绑定的
# class Student(object):
#     def __init__(self,name):
#         self.name = name
# s = Student('shp')
# print(s.name)
# s.name = 'shp2'
# print(s.name)
# 类的实例是直接在类中定义对所有实例生效
# class Student(object):
#     name = 'shp'
# s = Student()
# print(Student.name)
# s.name = 'Macel'
# print(s.name)
# 运行时绑定的优先级比较高
# del s.name
# print(Student.name)
# print(s.name)
# 就算删除了实例的动态绑定的name也没关系 都会调用实例的name属性
# 所以尽量类的属性不要跟实例的属性的名字一样

# 动态绑定方法
# class Student(object):
#     pass
# s = Student()
# def set_age(self,age):
#     self.age = age
# from types import MethodType
# s.set_age = MethodType(set_age,s)
# s.set_age(80)
# print(s.age)
# 但是它只对于当前实例生效
# 给类绑定
# Student.set_age = set_age
# s2 = Student()
# s2.set_age(20)
# print(s2.age)

# 使用__slots__限定类可以添加哪些属性
# class Student(object):
#     __slots__ = ('name','age')
# s = Student()
# s.name = 'shp'
# s.age = 100
# print(s.name)
# s.score = 100

# 不过__slots__只对当前类生效 对继承的类就不生效了
# class Gener(Student):
#     pass
# g = Gener()
# g.score = 100
# print(g.score)

# @property
# 这个是可以把一个方法当成属性来看待
# 属性分set和get @property就是get属性
# @xxx.setter 就是set属性
# 如果只设@property那么这个属性就是只读的 如果设上@xxx.setter 那么就是可读可写的
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2017-self.birth

s = Student()
s.birth = 2016
print(s.birth,s.age)
# 把一个方法变为set那么我们就可以对设置的属性值进行更多的检查和判断 让程序更加的健壮

