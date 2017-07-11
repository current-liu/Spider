# coding=utf-8

# 线程优先级队列（Queue）
"""Python和Queue模块中提供了同步的、线程安全的队列类，包括FIFO队列Queue，LIFO队列LifoQueue，
    和优先级队列PriorityQueue。这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列
    来实现线程间的同步。"""

import Queue
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["one", "two", "three", "four", "five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)


# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main thread"

