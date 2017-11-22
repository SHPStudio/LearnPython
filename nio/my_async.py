# 想要创建异步io我们需要自己去标记为coroutine
# 然后使用yield from 去做长时间的异步处理
# 我们可以使用async 去替换@asynio.coroutine
# 使用await去代替yield from
import asyncio

async def hello():
    print('Hello world')
    r = await asyncio.sleep(1)
    print('Hello world again')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
