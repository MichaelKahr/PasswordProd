import threading
import queue
from PasswordConsumer import PasswordConsumer
from PasswordProducer import PasswordProducer

myQueue = queue.Queue(maxsize=20)
condition = threading.Condition()

pwdProducer = PasswordProducer(queue=myQueue,condition=condition)
pwdConsumer = PasswordConsumer(queue = myQueue,condition = condition)
