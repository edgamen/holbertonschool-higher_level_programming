import threading
import urllib2

class LoripsumThread(threading.Thread):
    lock = threading.Lock()

    def __init__(self, filename):
        if type(filename) is  not str:
            raise Exception("Filename provided is not a string")
        self.filename = filename
        threading.Thread.__init__(self)

    ''' Append a lorem ipsum paragraph to a file, passed as argument to init '''
    def run(self):
        response = urllib2.urlopen('http://loripsum.net/api/1/short')
        snippet = response.read()

        LoripsumThread.lock.acquire()
        f = open(self.filename, 'a')
        f.write(snippet)
        f.close()
        LoripsumThread.lock.release()
