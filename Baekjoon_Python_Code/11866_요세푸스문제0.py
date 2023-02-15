# 출력초과란 무엇일까?

# from collections import deque
# import sys
# input = sys.stdin.readline
# N, K = map(int, input().rstrip().split())
# def Y(K, queue, Deque):
#     if len(queue) >= K:
#         for item in range(K-1):
#             queue.append(queue[0])
#             queue.popleft()
#         Deque.append(queue[0])
#         queue.popleft()
#         return queue, Deque
#     else:
#         for i in range(len(queue)):
#             Deque.append(queue[i])
#         return Deque
# queue = deque([])
# Deque = deque([])
# for i in range(1, N+1):
#     queue.append(i)
# for i in range(N-1):
#     Y(K, queue, Deque)
# print("<", end='')
# for i in range(len(Deque)-1):
#     print(Deque[i], end=', ')
# print(Deque[-1], end='')
# print(">", end='')
# -> 출력초과

from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
queue = deque([i+1 for i in range(N)])
print("<", end='')
for i in range(N-1):
    for j in range(K-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end='')
    if i != N-1:
        print(',', end=' ')
print(*queue, end='')
print(">")