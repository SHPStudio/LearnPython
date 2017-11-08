#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释表示是unix/linux系统可执行文件
# 第二行是代表该py文件编码方式为utf-8

'这个注释代表该模块的解释'

# 这个变量是代表模块的作者
__author__ = 'shape'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello module')
    elif len(args) == 2:
        print('Hello %s' % args[1])
    else:
        print('too many argument')

if __name__ == '__main__':
    test()