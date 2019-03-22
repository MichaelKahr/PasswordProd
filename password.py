import threading
import queue
from PasswordConsumer import PasswordConsumer
from PasswordProducer import PasswordProducer

myQueue = queue.Queue(maxsize=20)
myCondition = threading.Condition()

pwdProducer = PasswordProducer(queue=myQueue,condition=myCondition)
pwdConsumer = PasswordConsumer(queue = myQueue,conditon = myCondition)

pwdConsumer.start()
pwdProducer.start()
pwdConsumer.join()
pwdProducer.join()
