from collections import deque

queue = deque([1, 2, 3])

# appends an item to the end of the queue
queue.append(4)

print(queue)

# removes item from the begining of the queue

queue.popleft()

print(queue)

