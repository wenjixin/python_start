# coding=utf-8
print abs
f = abs
print f
print f(-1000)
# abs = 100
print abs
# op abs()


def add(x, y, f):
    print f(x) + f(y)

add(1, -2, abs)

"""
    map reduce
"""
print map(str, [1, 2, 3, 4])
print map(str, (1, 2, 3, 4))
print reduce(lambda x, y: x + y, (1, 2, 3, 4))
