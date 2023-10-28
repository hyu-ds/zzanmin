import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [0]*N
for num in range(M):
    i, j, k = map(int, input().rstrip().split())
    for l in range(i-1, j):
        arr[l] = k
print(*arr)