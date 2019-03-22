import threading
import queue

class Password():
    def __init(self, password):
        self.password = password

    def check(self,pwd):
        return self.password==password



class PasswordProducer(threading.Thread):
    def __init(self,queue,condition)__:
        self.queue = queue
        self.condition = condition

    def run(self):
        password = input("Please enter the password:")
        pwd = Password(password)
        try:
            self.queue.put(pwd,block=False)
            self.condition.notify()
        except queue.Full:
            self.condition.wait()

        self.condition.release()



