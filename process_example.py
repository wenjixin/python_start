#!/usr/bin/env python
# coding=utf-8
import os
import time
import random
from multiprocessing import Process, Pool, Queue

"""
多进程模式；
多线程模式；
多进程+多线程模式。
"""


# 子进程要执行的代码


def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())


def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:


def read(q):
    print 'read process start'
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__ == '__main__':
    # print 'Parent process %s.' % os.getpid()
    # p = Pool()
    # for i in range(10):
    #     p.apply_async(long_time_task, args=(i,))
    # print 'Waiting for all subprocesses done...'
    # p.close()
    # p.join()
    # print 'All subprocesses done.'
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pr = Process(target=read, args=(q,))
    pw = Process(target=write, args=(q,))
    # 启动子进程pr，读取:
    pr.start()
    # 启动子进程pw，写入:
    # pw.start()
    # 等待pw结束:
    # pw.join()

    time.sleep(60)
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
