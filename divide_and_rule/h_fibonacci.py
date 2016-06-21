import threading

class FibonacciThread(threading.Thread):

    ''' override initialization of Thread object '''
    def __init__(self, number):
        if type(number) is not int:
            raise Exception ("number is not an integer")
        self.number = number

    ''' when thread is started, compute fibonacci value of number in constructor '''
    def run(self):
        fibonacci_number = self.number - 1 + self.number - 2
        print "%d => %d" %(self.number, fibonacci_number)
