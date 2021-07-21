import time

from djworks.celery import add

for i in range(10):
    v = add.delay(3, 4)
    time.sleep(1)
