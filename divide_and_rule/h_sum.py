import threading

sum = 0

class Sum:

    def __init__(self, nb_threads, numbers):
        if type(nb_threads) is not int:
            raise Exception("nb_threads is not an integer")
        if type(numbers) is not list or not all(isinstance(n, int) for n in numbers):
            raise Exception("numbers is not an array of integers")
        self.threads = []

        for thread in nb_threads:
        ''' create new thread and give a slice of the array to compute the sum of: '''
            thread = SumThread('''slice of array''')
            self.threads += [thread]
            thread.start()

    def isComputing(self):
        for thread in self.threads:
            if thread.isAlive():
                return True
        return False

    def __str__(self):
        return str(total_sum)

class SumThread(threading.Thread):

    def __init__(self, numbers):
        if type(numbers) is not list or not all(isinstance(n, int) for n in numbers):
            raise Exception("numbers is not an array of integers")
        self.numbers = numbers
        threading.Thread.__init__(self)

    def run(self):
        global total_sum += sum(self.numbers)
