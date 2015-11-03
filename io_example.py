#!/usr/bin/env python
# coding=utf-8
import codecs
import os
import shutil


"""
File IO
"""
with open('./myapp.log', 'r') as f:
    for line in f.readlines():
        print(line.strip())

with open('./myapp.log', 'rb') as f:
    print f.read()

with codecs.open('./myapp.log', 'r', 'utf-8') as f:
    print f.read()  # u'\u6d4b\u8bd5'

with open('./myapp.log', 'w') as f:
    f.write('Hello, world!')
    f.write('ccc')

"""
os file && dir
"""
print os.name
print dir(os)

# not avalible in windows
# print os.uname()
print os.environ
print os.getenv('TMP')
print os.path.abspath('.')
# print os.mkdir(os.path.join(os.getenv('TMP'), 'python_test'))
print os.path.split('E:\code.space')
shutil.copyfile('myapp.log', 'myapp.log.bak')

print[x for x in os.listdir('.') if os.path.isdir(x)]


"""
序列化
"""


def sys_popen(cmd, out=True):
    _out = os.popen(cmd, 'r').read().strip()
    if out:
        return _out
    return None
print sys_popen('dir')


try:
    import cPickle as pickle
except ImportError:
    import pickle


d = dict(name='Bob', age=20, score=88)
print pickle.dumps(d)


with open('./myapp.log.bin', 'wb') as f:
    f.write(pickle.dumps(d))

with open('./myapp.log.bin', 'rb') as f:
    cc = pickle.load(f)
    print cc


import json

d = dict(name='Bob', age=20, score=88)
print json.dumps(d)

print json.loads(json.dumps(d))


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('tongwei', 1, 1)
print(json.dumps(s, default=student2dict))

print(json.dumps(s, default=lambda obj: obj.__dict__))


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
