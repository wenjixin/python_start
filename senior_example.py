# coding=utf-8

a_list = ['abc', 'def', 'ddd']

print a_list[0:3]
print a_list[-3:]
print a_list[-3:-1]
print a_list[-3:2]

a_tuple = (1, 2, 3, 4, 5)

# 前2个
print a_tuple[:2]
# 后两个
print a_tuple[-2:]
# 前5个，每个2个取一个
print a_tuple[:5:2]
# copy
print a_tuple[:]

"""
    字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
    在很多编程语言中，针对字符串提供了很多各种截取函数，其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
"""
print u'xxx'[:]

# iteration
a_dict = {'1': 1, 'c': 's'}
for key in a_dict:
    print key


for k, v in a_dict.iteritems():
    print k, v


from collections import Iterable
print isinstance('abc', Iterable)
print isinstance(123, Iterable)

# need index

for index, value in enumerate((1, 2, 3)):
    print index, value


for x, y in [(1, 2)]:
    print x, y

"""
   list builder
"""
print range(1, 200, 3)
print[x * x for x in range(1, 11)]
print[x * x for x in range(1, 11) if x % 3 == 0]
print[m + n for m in 'abc' for n in 'xyz']
import os
print[d for d in os.listdir('.')]

L = ['Hello', 'World', 19, 'IBM', 'Apple']
print[s.lower() if isinstance(s, str) else s for s in L]


"""
    通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

"""
L = [x * x for x in range(10)]
print L
g = (x * x for x in range(10))
print g
for n in g:
    print n


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1


def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
for n in fib_g(10):
    print n
