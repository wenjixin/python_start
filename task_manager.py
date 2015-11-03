# coding=utf-8
import time
import Queue
import random
from multiprocessing.managers import BaseManager

task_queue = Queue.Queue()
result_queue = Queue.Queue()


class QueueManager(BaseManager):
    """ for QueueManager"""
    pass

QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

manager = QueueManager(address=('', 5000), authkey='abc')
manager.start()
task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(100000):
    n = random.randint(0, 10000)
    print('put new task %s ' % n)
    task.put(n)

# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get()
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
