import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
arr = [0]*N
for num in range(N):
    arr[num] = num+1
for num in range(M):
    i, j = map(int, input().rstrip().split())
    temp = arr[j-1]
    arr[j-1] = arr[i-1]
    arr[i-1] = temp
print(*arr)