# 序列化
# 序列化是要把内存中的不想断电删除一些比较重要的数据持久化到磁盘
# 当下次运行程序的时候可以从磁盘反序列化我们想要的数据
# pickle模块可以进行简单的序列化 不过他的缺点就是只能用于python不能用于其他语言

# 序列化
import pickle
# d = dict(name='shp',age=20,city='北京')
# with open('d:/mys.shp','wb') as f:
#     print(pickle.dump(d, f))

# 反序列化
d = None
with open('d:/mys.shp','rb') as f:
    d = pickle.load(f)
print(d)