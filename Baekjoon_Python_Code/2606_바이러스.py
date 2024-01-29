import sys
input = sys.stdin.readline

def DFS_Iter(G, s):
    S = [s]
    isVist = []
    while len(S) != 0:
        u = S.pop()
        if u not in isVist:
            isVist.append(u)
            for v in range(len(G[u])):
                if G[u][v] == 1 and v not in isVist:
                    S.append(v)
    return isVist

N = int(input())
V = int(input())

G = [[0 for v in range(N+1)] for u in range(N+1)]

for v in range(V):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1

visitList = DFS_Iter(G, 1)

print(len(visitList)-1)