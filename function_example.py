# coding=utf-8
print abs(-100)
print cmp(-1, -2)


# type conveter
print int('100')
print unicode('100')
print bool('')
print bool(None)
print bool('111')

# funcation rename
a = abs
print a(-10000)


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Not support type')
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-100)


def donothing():
    pass

# indeed it return a tuple


def return_mutiple_value(x, y):
    return x, y

x, y = return_mutiple_value(1, 2)

print x, y

x = return_mutiple_value(1, 2)

print(x)


# funcation param
def func2(x, y=1):
    print x, y

func2(0)


# default value 的坑:  Python函数在定义的时候，默认参数L的值就被计算出来了,so 默认参数必须是不可变对象才行。

def keng(L=[]):
    L.append('END')
    return L

print keng()
print keng()


# should

def normal(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print normal()
print normal()

# dynamic paramater,很实用


def cal(*nums):
    sum = 0
    for n in nums:
        sum = sum + n
    return sum

print cal(1, 2, 3, 4, 5, 6)

num = [1, 2, 3, 4, 5, 6]
print cal(*num)
num = (1, 2, 3, 4, 5, 6)
print cal(*num)


def extend_method(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

extend_method('abc', 'test', other=1)


kwd = {'ad': 'b', 'cd': 'd'}

extend_method('abc', 'def', **kwd)


# combined param, notice the kw cannot be same with pre paramaters
def combined_fun(a, b, *c, **kw):
    print a, b, c, kw

combined_fun('a', 'b', *num, **kwd)

# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

args = [1, 2, 3, 4]
kw = {}
combined_fun(*args, **kw)


def common_method(*args, **kwargs):
    print args
    print kwargs


def recursive(n=1):
    if n == 1:
        return 1
    return n * recursive(n - 1)


print recursive(5)


# 优化递归
def fact(n):
    return fact_iter(n, 1)

"""
    尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
    but python 没有

    当编译器检测到一个函数调用是尾递归的时候，它就覆盖当前的活动记录而不是在栈中去创建一个新的。编译器可以做到这点，因为递归调用是当前活跃期内最后一条待执行的语句，于是当这个调用返回时栈帧中并没有其他事情可做，因此也就没有保存栈帧的必要了。通过覆盖当前的栈帧而不是在其之上重新添加一个，这样所使用的栈空间就大大缩减了，这使得实际的运行效率会变得更高。
"""


def fact_iter(num, product):
    if num == 1:
        return product
    else:
        return fact_iter(num - 1, num * product)
