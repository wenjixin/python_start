#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals
from __future__ import division

' a test module '

__author__ = 'tongwei'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__ == '__main__':
    test()


try:
    import cStringIO as StringIO
except ImportError:  # 导入失败会捕获到ImportError
    import StringIO


try:
    import json  # python >= 2.6
except ImportError:
    import simplejson as json  # python <= 2.5


"""
    作用域-函数或变量
"""
__hello__ = 1
__notvisible = 2


import sys
print sys.path


print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)


print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3
