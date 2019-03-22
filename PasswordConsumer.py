import threading
import queue

class PasswordConsumer(threading.Thread):
    def __init__(self,queue,conditon):
        self.queue = queue
        self.conditon = conditon

    def run(self):
        pw_file = open("list.txt","r")
        while True:
            self.conditon.acquire()
            try:
                pwd = self.queue.get(block=False)
                self.conditon.notify()
            except queue.Empty:
                self.conditon.wait()
            self.conditon.wait()
            for x in pw_file:
                res = pwd.check(x)
                if res:
                    print("Password found")
                break

