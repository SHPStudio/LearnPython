# 测试worker
import time,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

# 从网络上获取
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 链接到服务器
serverAddr = '127.0.0.1'
manager = QueueManager(address=(serverAddr,5000),authkey=b'abc')

# 开启链接
manager.connect()

# 获取对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 开始获取任务并进行处理然后把处理后的数据放回队列上
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run the task %d * %d' % (n * n))
        r = '%d * %d = %d' % (n,n,n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty')

# 处理结束
print('task is end')