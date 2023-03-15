"""
5. Data Structures, 13. Queues

Queue
FIFO: First In First Out

Can use a list to implement a queue.
"""
from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")
