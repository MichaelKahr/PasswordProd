import threading
import queue

class PasswordConsumer(threading.Thread):
    def __init__(self,queue,conditon):
        threading.Thread.__init__(self)
        self.queue = queue
        self.conditon = conditon

    def run(self):
        while True:
            pw_file = open("list.txt","r")
            pwd = ""
            self.conditon.acquire()
            try:
                pwd = self.queue.get(block=False)
                self.conditon.notify()
            except queue.Empty:
                #print("consumer waiting")
                self.conditon.wait()
                #print("consumer waiting")
            self.conditon.release()
            #print("condition released")
            if pwd != "":
                for x in pw_file:
                    res = pwd.check(x.split("\n")[0])
                    if res:
                        print("Password found")
                        break

