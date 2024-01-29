import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

g1 = [[0 for m in range(N+1)] for n in range(N+1)]
g2 = [[0 for m in range(N+1)] for n in range(N+1)]

for v in range(M):
    a, b = map(int, input().split())
    g1[a][b] = 1
    g1[b][a] = 1
    g2[a][b] = 1
    g2[b][a] = 1

def BFS(g, u):
    queue = deque([u])
    s = []
    while len(queue) != 0:
        u = queue.popleft()
        if u not in s:
            s.append(u)
            for v in range(len(g[0])):
                if g[u][v] == 1:
                    if v not in queue:
                        queue.append(v)
                    g[u][v] = 0
    return s

def DFS(g, V):
    queue = deque([V])
    s = []
    i = 0
    while len(queue) != 0:
        u = queue.pop()
        if u not in s:
            s.append(u)
            for v in range(len(g[0])-1, 0, -1):
                if g[u][v] == 1:
                    if v not in s:
                        queue.append(v)
                    g[u][v] = 0
        i+=1

    return s

print(*DFS(g1, V))
print(*BFS(g2, V))