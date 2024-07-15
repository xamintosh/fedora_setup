import time
import sys

counter = 5
for i in range(5):

    sys.stdout.write(str(counter))
    sys.stdout.write('..')
    sys.stdout.flush()
    time.sleep(1)
    counter = counter - 1
