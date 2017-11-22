# 分布式进程
# 可以把不同的进程放到多台机器上
# 比如我们有一个任务处理系统
# 这个系统遵循的结构是master-worker的模式
# 这个master主要是发布任务的 worker主要是处理任务的
# multiProcess下的子模块managers支持把多个进程放到其他地方
# 首先创建服务进程
import time,random,queue
from multiprocessing.managers import BaseManager


# 发送队列
task_queue = queue.Queue()
# 结果队列
result_queue = queue.Queue()

# 从basemanager继承QueueManager
class QueueManager(BaseManager):
    pass

# 把两个queue注册到网络上
QueueManager.register('get_task_queue',callable= lambda: task_queue)
QueueManager.register('get_result_queue',callable=lambda: result_queue)

# 绑定端口 设置链接密码
manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
# 开始服务
manager.start()

# 从网络上访问queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进去
for i in range(10):
    n = random.randint(0,10000)
    print('Put task %s' % n)
    task.put(n)
# 从result队列中获取数据
print('Try to get result。。。。')
for i in range(10):
    r = result.get(timeout=10)
    print('Result=%s' % r)
# 结束
manager.shutdown()
print('master end')