# 协程
# 协程是一个线程 在执行子程序的过程中可以进行类似cpu的中断去执行其他子程序
# 适当的时候在返回回来继续执行
# 很像多线程的执行方式 不过多线程的线程切换是由系统决定
# 协程的程序切换是由程序代码控制的 执行效率比较高
# 他的好处是避免了多线程互相等待死锁的现象因为他只有一个线程
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[COMSUMER] consuming %s。。。' % n)
        r = '200 ok'

def provide(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PROVIDE] providing %s...' % n)
        r = c.send(n)
        print('[CONSUMER] consuming %s...' % r)
    c.close()

c = consumer()
provide(c)
