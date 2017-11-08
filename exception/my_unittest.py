# 单元测试
# python自带的unittest.TestCase可以支持单元测试
# 单元测试中的测试方法带有断言即可
# 导入自己开发的模块
# 我们测试类必须要继承unittest.TestCase
# 我们的测试方法一定要以test_xxx开头否则不认为是测试方法
import unittest
from mydict import Dict

class TestDict(unittest.TestCase):

    # 如果要是在每次调用测试方法的时候想在之前或者之后做一下处理 比如一开始链接数据库或者之后断开相应链接之类的
    def setUp(self):
        print('start...')

    def tearDown(self):
        print('end....')


    def test_init(self):
        d = Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# 运行测试用例
# if __name__ == '__main__':
#     unittest.main()