import threading, time

class my_thread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ('open thread: ' + self.name)
        # lock
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # unlock
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()

thread1 = my_thread(1, 'thread 1', 1)
thread2 = my_thread(2, 'thread 2', 2)

thread1.start()
thread2.start()