# 集合工具类 collections
# namedtuple
# 比如我们定义一个Point坐标 其实他就有两个变量 x,y或者表示一个圆他有坐标和半径
# 其实这是死的一个tuple就可以表示
# 使用这个就可以很容易的去给一个固定的tuple去命名去生成一个tuple的子类
# from collections import namedtuple
# Point = namedtuple('Point',['x','y'])
# point = Point(1,2)
# print(point)

# deque 双向链表 比较适合增加删除等等 碰到大量数据时 比list效率要高
# 所以比较适合队列和栈
# from collections import deque
# d = deque([1,2,3,4])
# print(d)
# d.append('30')
# print(d)
# d.appendleft('44')
# print(d)
# d.pop()
# print(d)
# d.popleft()
# print(d)

# 我们使用dict的时候经常碰到key不存在的时候会报异常
# 我们可以使用defaultdict来给不存在的key设置一个默认值 比如N/A
# 这样他就不会报错了
# from collections import defaultdict
# dd = defaultdict(lambda :'N/A')
# dd['shp'] = 'shp'
# print(dd['shp'])
# print(dd['sss'])

# orderdict可以让dict按照插入的顺序排序

# Counter 计算字符出现次数
from collections import Counter
c = Counter()
for ch in 'adfakjgsd':
    c[ch] = c[ch] + 1
print(c)
