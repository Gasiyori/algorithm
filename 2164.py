from sys import stdin, stdout
from collections import deque

queue = deque([i for i in range(1, int(stdin.readline().rstrip()) + 1)])

while (len(queue) > 1):
    queue.popleft()
    queue.append(queue.popleft())

stdout.write(str(queue.pop()))