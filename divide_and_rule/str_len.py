import sys
import threading

class StrLenThread(threading.Thread):

    ''' overloading of init function from parent '''
    def __init__(self, word):
        threading.Thread.__init__(self)
        if type(word) is not str:
            raise Exception("word is not a string")
        self.word = word

    ''' add length of word to global var whenever thread is created '''
    def run(self):
        global total_str_length
        total_str_length += len(word)

text = sys.argv[1:]
if len(text) == 0:
    total_str_length = len(text)
else:
    total_str_length = len(text) - 1

threads = []

for word in text:
    thread = StrLenThread(word)
    threads += [thread]
    thread.start()

for t in threads:
    t.join()

print "%d" % total_str_length
