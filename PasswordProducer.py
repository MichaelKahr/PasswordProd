import threading
import queue

class Password():
    def __init__(self, password):
        self.password = password

    def check(self,pwd):
        #print("in check method: *"+self.password+"* Password to compare to:*"+pwd+"*")
        if self.password==pwd:
            return True
        return False

class PasswordProducer(threading.Thread):
    def __init__(self,queue,condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition

    def run(self):
        while True:
            password = input("")
            pwd = Password(password)
            self.condition.acquire()
            try:
                self.queue.put(pwd,block=False)
                self.condition.notify()
                #print("condition notified")
            except queue.Full:
                self.condition.wait()
                #print("condition waiting")

            self.condition.release()
            #print("conditin released")
