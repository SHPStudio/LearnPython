## 可以把一个方法标记为一个coroutine 其实也就是标记为generator
# 他可以把这个coroutine扔到eventloop中去执行 并且在这个方法里还可以调用别的genrerator
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print('Hello begin')
#     # 异步调用
#     r = yield from asyncio.sleep(1)
#     print('Hello again')
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

# 他并不会阻塞主线程 我们可以往eventloop中放入多个task任务去执行
import threading
import asyncio

def hello():
    print('Hello world! (%s)' % threading.current_thread().name)
    r = yield from asyncio.sleep(1)
    print('Hello world again (%s)' % threading.current_thread().name)

loop = asyncio.get_event_loop()
task = [hello(),hello()]
loop.run_until_complete(asyncio.wait(task))
loop.close()

# 这样就可以支持并发了
# 比如我们想要同时获取很多网站的信息 就可以封装一个task 去并发异步的去获取
# 异步操作是yield from 去做的

