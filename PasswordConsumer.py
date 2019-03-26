import threading
import queue

class PasswordConsumer(threading.Thread):
    def __init__(self,queue,conditon):
        threading.Thread.__init__(self)
        self.queue = queue
        self.conditon = conditon

    def run(self):
        pw_file = open("list.txt","r").read()
        while True:
            self.conditon.acquire()
            try:
                pwd = self.queue.get(block=False)
                self.conditon.notify()
            except queue.Empty:
                print("exception")
                self.conditon.wait()
            self.conditon.release()

            for x in pw_file:
                res = pwd.check(x)
                if res:
                    print("Password found")
                break

