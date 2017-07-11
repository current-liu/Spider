# coding=utf-8
"""Python网络编程
    Python提供了两个级别的网络服务：
        低级别的网络服务支持Socket，它提供了标准的BSD Socket API，可以访问底层操作系统Socket接口的全部方法
        高级别的网络服务模块SocketServer，它提供了服务器中心类，可以简化网络服务器的开发"""

# Python中使用线程有两种方式：函数或者用类来包装线程对象
# 函数式：调用thread模块中的start_new_thread()函数来产生新线程
#           thread.start_new_thread(function,args[,kwargs])
import thread
import time

# def clock(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print threadName, time.ctime(time.time())
#
# try:
#     thread.start_new_thread(clock, ("Thread-1", 2, ))
#     thread.start_new_thread(clock, ("Thread-2", 4, ))
# except:
#     print "Error: unable to start thread"
# while 1:
#     pass

"""线程模块：
    Python通过两个标准库thread和threading提供对线程的支持，thread提供了低级别的、原始的线程及一个简单的锁
    thread模块提供的其他方法：
        threading.curreThread()：
        threading.enumerate()：
        threading.activeCount()
    除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法：
        run()
        start()
        join([time])
        isAlive()
        getName()
        serName()"""

# 使用Threading模块创建线程：
# 直接从threading.Thread继承，然后重写__init__方法和run方法

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting" + self.name
        print_time(self.name, self.counter, 5)
        print "EXiting" + self.name

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        print threadName, time.ctime(time.time())
        counter -= 1

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

print "Exiting Main Thread"