"""
9. Python Standard Library, 09. Working with Timestamps

datetime and time modules in Python.

"""
import time


def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)
