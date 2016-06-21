import threading

class ReverseStrThread(threading.Thread):

    sentence = ""
    lock = threading.Lock()

    def __init__(self, word):
        threading.Thread.__init__(self)
        if type(word) is not str:
            raise Exception("word is not a string")
        self.word = word

    def run(self):
        reverse_word = self.word[::-1]
        ReverseStrThread.lock.acquire()
        ReverseStrThread.sentence += reverse_word
        ReverseStrThread.sentence += " "
        ReverseStrThread.lock.release()
