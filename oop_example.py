#!/usr/bin/env python
# coding=utf-8


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

"""
   也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

   有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。


"""
bart.age = 8
print bart.age
bart.__name = 10
print bart.__name
bart.print_score()
print bart._Student__name
print bart._Student__score
# print lisa.age


import types
print type('abc') == types.StringType
print isinstance('a', (str, unicode))


print dir('ABC')


"""
使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：

除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。

"""


class Student(object):
    __slots__ = ('name', 'age')


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


"""
Mixin
"""


class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, name):

        return Chain('%s/%s' % (self._path, name))


print Chain().status.user.timeline.list

print Chain().users('michael').repos('cc')


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))


"""
使用元类,TODO
"""
