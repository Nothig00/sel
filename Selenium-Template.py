

import threading

import time

maxthreads = 5

sema = threading.Semaphore(value=maxthreads)

threads = list()

def task(i):

    sema.acquire()

    print("start %s" % (i,))

    time.sleep(2)

    sema.release()

for i in range(10):

    thread = threading.Thread(target=task,args=(str(i)))

    threads.append(thread)

    thread.start()
