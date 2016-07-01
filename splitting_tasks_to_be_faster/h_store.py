import threading
import time
import random

class Store:

    def __init__(self, item_number, person_capacity):
        if type(item_number) is not int:
            raise Exception("Number of items provided is not an int")
        if type(person_capacity) is not int:
            raise Exception("Person capacity provided is not an int")
        self.item_number = item_number
        self.__sema = threading.Semaphore(person_capacity)

    ''' when a person enters, add count towards sema capacity '''
    def enter(self):
        self.__sema.acquire()

    ''' simulate person buying an item and release sema once for person leaving'''
    def buy(self):
        time.sleep(random.uniform(5,10))
        if (self.item_number) <= 0:
            self.__sema.release()
            return False

        self.item_number -= 1
        self.__sema.release()
        return True;
