import threading

class OrderedArray:

    list = []

    def __init__(self):
        self.threads = []

    def add(self, number):
        if type(number) is not int:
            raise Exception("number is not an integer")
        thread = OrderedArrayThread(number)
        self.threads += [thread]
        thread.start()

    def isSorting(self):
        for thread in self.threads:
            if thread.isAlive():
                return True
        return False

    def __str__(self):
        return str(OrderedArray.list)
        '''return ', '.join(map(str, OrderedArray.list))'''

class OrderedArrayThread(threading.Thread):

    lock = threading.Lock()

    def __init__(self, number):
        if type(number) is not int:
            raise Exception("number is not an integer")
        self.number = number
        threading.Thread.__init__(self)

    def run(self):

        OrderedArrayThread.lock.acquire()

        if len(OrderedArray.list) == 0:
            OrderedArray.list.append(self.number)
            OrderedArrayThread.lock.release()
            return
        for i in OrderedArray.list:
            if self.number < i:
                OrderedArray.list.insert(i, self.number)
                OrderedArrayThread.lock.release()
                return
        OrderedArray.list.append(self.number)
        OrderedArrayThread.lock.release()
