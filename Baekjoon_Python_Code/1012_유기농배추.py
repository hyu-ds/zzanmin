import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def graphSearch(g:list, i, j):
    g[i][j] = 0
    if i > 0 and g[i-1][j] == 1:
        g = graphSearch(g, i-1, j)
    if i < len(g)-1 and g[i+1][j] == 1:
        g = graphSearch(g, i+1, j)
    if j > 0 and g[i][j-1] == 1:
        g = graphSearch(g, i, j-1)
    if j < len(g[0])-1 and g[i][j+1] == 1:
        g = graphSearch(g, i, j+1)
    return g

T = int(input())         

for t in range(T):
    N, M, K = map(int, input().split())

    field = [[0 for m in range(M)] for n in range(N)]

    for k in range(K):
        n, m = map(int, input().split())
        field[n][m] = 1

    cnt = 0
    
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                field = graphSearch(field, i, j)
                cnt += 1
    print(cnt)
    