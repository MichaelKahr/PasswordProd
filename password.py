import threading
import queue
from PasswordConsumer import PasswordConsumer
from PasswordProducer import PasswordProducer

myQueue = queue.Queue(maxsize=20)
myCondition = threading.Condition()

pwdProducer = PasswordProducer(queue=myQueue,condition=myCondition)
pwdConsumer = PasswordConsumer(queue = myQueue,conditon = myCondition)
pwdConsumer2 = PasswordConsumer(queue = myQueue,conditon = myCondition)
pwdProducer.start()
pwdConsumer.start()
pwdConsumer2.start()
pwdProducer.join()
pwdConsumer.join()
pwdConsumer2.join()

