import threading

total_sum = 0

class Sum:

    def __init__(self, nb_threads, numbers):

        if type(nb_threads) is not int:
            raise Exception("nb_threads is not an integer")
        if type(numbers) is not list or not all(isinstance(n, int) for n in numbers):
            raise Exception("numbers is not an array of integers")

        global total_sum
        total_sum = 0

        self.threads = []
        list_slices = []

        ''' divides array into roughly nb_number chunks '''
        for x in range(0, len(numbers), len(numbers)/nb_threads):
            slice = numbers[x:x+len(numbers)/nb_threads]
            list_slices.append(slice)

        ''' if there was some remainder, resulting in extra chunk, add those ints
            to the previous chunk '''
        if len(list_slices) > nb_threads:
            list_slices[nb_threads - 1] += list_slices[nb_threads]

        for slice in list_slices[: nb_threads]:
            thread = SumThread(slice)
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

    lock = threading.Lock()

    def __init__(self, numbers):
        if type(numbers) is not list or not all(isinstance(n, int) for n in numbers):
            raise Exception("numbers is not an array of integers")
        self.numbers = numbers
        threading.Thread.__init__(self)

    def run(self):
        global total_sum
        total_sum += sum(self.numbers)
