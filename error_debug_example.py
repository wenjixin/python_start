#!/usr/bin/env python
# coding=utf-8

import logging
import pdb

logging.basicConfig(level=logging.INFO)

try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    logging.exception(e)
finally:
    print 'finally...'
print 'END'


try:
    print 'try...'
    # pdb.set_trace()
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
finally:
    print 'finally...'
print 'END'


"""
常见的错误类型和继承关系:https://docs.python.org/2/library/exceptions.html#exception-hierarchy
"""


# err.py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


# python -O err.py,忽略断言


"""
单元测试
"""


class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
