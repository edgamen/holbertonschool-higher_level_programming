import threading

class FibonacciThread(threading.Thread):

    ''' override initialization of Thread object '''
    def __init__(self, number):
        threading.Thread.__init__(self)
        if type(number) is not int:
            raise Exception ("number is not an integer")
        self.number = number

    ''' when thread is started, compute fibonacci value of number in constructor '''
    def run(self):
        j = 0
        k = 1
        for i in range(1, self.number):
            fibonacci_number = j + k
            j = k
            k = fibonacci_number
        print "%d => %d" %(self.number, fibonacci_number)
