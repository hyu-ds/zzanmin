from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
def process(queue):
    queue.popleft()
    temp = queue[0]
    queue.popleft()
    queue.append(temp)
    return queue
queue = deque([])
for num in range(1, N+1):
    queue.append(num)
for i in range(N-1):
    process(queue)
print(*queue)