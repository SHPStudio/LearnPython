# 多进程
# 一般os中的fork()函数可以在unix/linux系统中创建进程
# 但是fork()函数在windows系统中并不适用
# 所以我们需要使用 multiprocessing去创建进程
# import os
# from multiprocessing import Process
# 子进程要运行的代码
# def run_proc(name):
#     print('run the child process %s (%s) ...' % (name, os.getpid()))
# 主进程
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('child process will start')
#     p.start()
#     p.join()
#     print('child process end')
# start开启线程
# join等待线程执行结束

# 启动多个进程可以使用进程池
# 如果使用close()函数那么就代表无法再创建新的进程了
# join等待所有子进程结束
# from multiprocessing import Pool
# import os,time,random
# def long_time_task(name):
#     print('Run task %s (%s)' % (name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 10)
#     end = time.time()
#     print('Task %s run %0.2f seconds' % (name,(end-start)))
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(0,5):
#         p.apply_async(long_time_task,args=(i,))
#     print('wait all subprocess end')
#     p.close()
#     p.join()
#     print('all subprocess end')
# Pool(4)是代表可以同时跑的进程数
# 默认跟cpu核数相同比如如果是8核的那么需要9个进程才能看出来最后一个进程迟缓开启

# 子进程
# 很多情况下子进程为外部的进程 所以我们可以使用subprocess方便的创建子进程并进行一些操作
# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['ping','www.python.org'])
# print('Exit code:',r)
# call 相当于在命令行上敲 nslookup www.python.org
# 如果需要输入的话需要使用communicate
# print('$ nslookup www.python.org')
# r = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# output,err = r.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('gbk'))
# print('Exit code:',r.returncode)
# 这个可以执行一些系统命令

# 进程间通信
# 可以使用Queue队列或者使用Pipe管道来交换数据
import os,time,random
from multiprocessing import Process,Queue

# 写入
def write(q):
    print('Process to write:%s' % os.getpid())
    for value in ['A','B','C']:
        print('Put value %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())
# 读取
def read(q):
    print('Process to read:%s' % os.getpid())
    while(True):
        value = q.get(True)
        print('Get value %s from queue...' % value)

if __name__=='__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()