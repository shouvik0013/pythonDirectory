from threading import Thread, Condition
from time import sleep


class Producer:

    def __init__(self):
        self.lst = list()
        self.cv = Condition()

    
    def produce(self):
        # lock the condition object
        self.cv.acquire()

        for i in range(1,11):
            self.lst.append(i)
            sleep(1)
            print('Item produced...')
        
        self.cv.notify_all()

        self.cv.release()



class Consumer:

    def __init__(self, prod:Producer):
        self.prod = prod

    
    def consume(self):
        # get lock on cv
        self.prod.cv.acquire()

        # wait untill producer finishes
        self.prod.cv.wait(timeout=0)

        print(self.prod.lst)

        self.prod.cv.release()


p = Producer()

c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()

t1.join()
t2.join()