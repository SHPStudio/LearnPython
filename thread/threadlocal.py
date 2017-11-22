# 让每个线程也有自己的局部变量
# 这个功能可以使用ThreadLocal来实现
import threading

# 全局临时变量ThreadLocal
local_school = threading.local()

def print_student():
    std = local_school.student
    print('Hello %s in(%s)' % (std,threading.current_thread().name))

def set_student(name):
    local_school.student = name
    print_student()

t1 = threading.Thread(target=set_student,args=('shp1',),name='Thread-A')
t2 = threading.Thread(target=set_student,args=('txte2',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 所以threadlocal虽然是全局的，但是他对于每个线程都是独立的互不干扰
# 他很好的解决了同一个线程调用不同函数相互传参的问题