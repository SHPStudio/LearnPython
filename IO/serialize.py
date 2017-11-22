# 序列化
# 序列化是要把内存中的不想断电删除一些比较重要的数据持久化到磁盘
# 当下次运行程序的时候可以从磁盘反序列化我们想要的数据
# pickle模块可以进行简单的序列化 不过他的缺点就是只能用于python不能用于其他语言

# 序列化
# import pickle
# d = dict(name='shp',age=20,city='北京')
# with open('d:/mys.shp','wb') as f:
#     print(pickle.dump(d, f))

# 反序列化
# d = None
# with open('d:/mys.shp','rb') as f:
#     d = pickle.load(f)
# print(d)

# 但是使用picking方法的序列化的只有python可以用所以我们可以使用json序列化使别的语言也可以使用
import json
# d = dict(name='shp',age=20,city='北京')
# with open('d:/testjson.shp','w') as f:
#     print(json.dump(d,f))
# d = {}
# with open('d:/testjson.shp','r',encoding='utf-8') as f:
#     temp = f.read()
#     d = json.loads(temp)
# print(d)

# 序列化类
# 如果我们直接序列化一个类的话就会报typeerror的错误
# 所以一般我们需要做一个转换函数 把类转换成dict
class Student(object):
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
def student2dict(stu):
    return {
        'name':stu.name,
        'age':stu.age,
        'city':stu.city
    }
# s = Student('shp',20,'北京')
# print(json.dumps(student2dict(s)))
# 我们可以使用default参数把任意对象变成可序列化的对象
# print(json.dumps(s,default=student2dict))
# 更方便的可以使用lambda表达式去做对象有个默认__dict__变量 就是存储变量信息的
# print(json.dumps(s,default=lambda obj:obj.__dict__))

# 反序列化
# 反序列化也是一样需要对dict转换成对象做一个转换函数 然后使用object_hook函数进行转换
temp = '{"age": 20, "city": "\u5317\u4eac", "name": "shp"}'
def dict2student(str):
    return Student(str['name'],str['age'],str['city'])
print(json.loads(temp,object_hook=dict2student))