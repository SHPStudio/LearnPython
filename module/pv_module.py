# 私有模块
def _private_1(name):
    print("Hello %s" % name)
def _private_2(name):
    print("Hi %s" % name)
def greeting(name):
    if len(name) > 3:
        _private_1(name)
    else:
        _private_2(name)