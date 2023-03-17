import sys
from collections import deque

sys.stdin = open('input.txt')

N = int(input())

queue = deque()

for i in range(N):
    queue.append(i + 1)

while True:
    if len(queue) == 1:
        break
    else:
        queue.popleft()
        queue.append(queue.popleft())

print(*queue)

