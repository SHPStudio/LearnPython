# 多线程
# 线程编程主要是_thread还有threading模块 _thread是低级模块 threading是高级模块 threading把_thread进行了封装
# 所以我们使用threading就可以了
# import time,threading
# def loop():
#     print('thread %s is runing' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >> %s' % (threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s is end' % threading.current_thread().name)
#
# print('threa %s is runing' % threading.current_thread().name)
# t = threading.Thread(target=loop,name='localthread')
# t.start()
# t.join()
# print('thread %s is end' % threading.current_thread().name)

# 多进程的变量是每个进程一份副本 但是多线程的变量是共用的
# 这样多个线程一起访问改变这个变量的时候很可能就会变乱
# import threading,time
#
# # 共有变量
# balence = 0
#
# def change_it(n):
#     global balence
#     balence = balence + n
#     balence = balence - n
#
# def chang_run(n):
#     for i in range(1000000):
#         change_it(n)
#
# t1 = threading.Thread(target=chang_run,args=(5,))
# t2 = threading.Thread(target=chang_run,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balence)
# 我们可以看到balance的值并不是0
# 这因为在赋值的时候系统会在中间插入一个临时变量
# balance = balance + 1
# x = balance + 1
# balance = x
# 如果x还没赋给balance的时候系统就把cpu分给别的线程了那么这个balance的值就错误了
# 所以我们需要在操作这个的时候必须同时只能让一个线程去操作
# 这个时候我们就需要使用锁了
import threading,time
lock = threading.Lock()
# 共有变量
balence = 0

def change_it(n):
    global balence
    balence = balence + n
    balence = balence - n

def chang_run(n):
    for i in range(1000000):
        # 获得锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 用完释放锁
            lock.release()

t1 = threading.Thread(target=chang_run,args=(5,))
t2 = threading.Thread(target=chang_run,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balence)

# 注意一定用完一定要释放锁否则将会是个死线程别的线程无法进行操作了
# python的多线程只能使用一个cpu核心