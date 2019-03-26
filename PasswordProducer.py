import threading
import queue

class Password():
    def __init__(self, password):
        self.password = password

    def check(self,pwd):
        return self.password==pwd



class PasswordProducer(threading.Thread):
    def __init__(self,queue,condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition

    def run(self):
        password = input("Please enter the password:")
        pwd = Password(password)
        self.condition.acquire()
        try:
            self.queue.put(pwd,block=False)
            self.condition.notify()
        except queue.Full:
            self.condition.wait()

        self.condition.release()
