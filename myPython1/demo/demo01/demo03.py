#!/usr/bin/env python
# coding=utf-8
"""
Created on 2017/7/30 16:56

base Info
"""
import os

__author__ = 'liuchao'
__version__ = '1.0'

import sys
from multiprocessing import Process

reload(sys)
sys.setdefaultencoding('utf-8')


def run_proc(name):
    print 'child process %s (%s) Running...' % (name, os.getpid())


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    for i in range(5):
        p = Process(target=run_proc, args=(str(i)))
        print 'Process will start.'
        p.start()
    p.join()
    print 'Process end.'
