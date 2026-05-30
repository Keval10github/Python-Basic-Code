from collections import deque
# FIFO (First In, First Out)
queue = deque(["Alice", "Bob", "Charlie"])
queue.append("David") # Enqueue
print("Served:", queue.popleft()) # Dequeue removes the first item
print("Current Queue:", list(queue))