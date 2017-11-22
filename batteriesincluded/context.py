# 上下文管理
# 我们一般使用打开网络连接或者文件资源的时候
# 需要在使用的时候创建一个网络连接对象或者文件流等等
# 在使用完成之后需要自己把资源给释放掉
# 正常我们需要使用try..finally的形式
# 这么写太麻烦了 所以我们有简单的形式就是使用with
# 他的原理就是在类中进行了上下文的管理
# 使用__enter__(self) 和__exit__对类进行处理
# class Query(object):
#     def __init__(self,name):
#         self.name = name
#
#     def __enter__(self):
#         print('Begin')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             print('Error')
#         else:
#             print('Exit')
#
#     def query(self):
#         print('query s is info %s' % self.name)
#     def query2(self):
#         print('query 2 is info %s' % self.name)
#
# with Query('bob') as q:
#     q.query()
#     q.query2()
# 这样他就会在实例化实例的时候还有使用完成的时候都会调用enter和exit方法去做一些自定义的处理

# 这么写还是可能会有点儿麻烦
# contextlib提供了更简便的写法
# from contextlib import contextmanager
# class Query(object):
#
#     def __init__(self,name):
#         self.name = name
#
#     def query(self):
#         print('Query de info %s' % self.name)
# @contextmanager
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')
#
# with create_query('shp') as q:
#     q.query()
# @contextmanager 他可以接受一个构造器然后通过yield把变量抛出给 with 。。 as var 的变量用

# 如果一个对象没有实现上下文那么可以通过closing把对象做一下包装，让对象实现上下文
from contextlib import closing
from urllib.request import urlopen

with(closing(urlopen('https://www.python.org'))) as pages:
    for line in pages:
        print(line)

