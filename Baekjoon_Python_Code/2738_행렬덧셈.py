import sys
input = sys.stdin.readline

N, M = map(int, input().strip('\n').split())

arr1 = []
arr2 = []
arr = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    arr1.append(list(map(int, input().strip('\n').split())))
for i in range(N):
    arr2.append(list(map(int, input().strip('\n').split())))

for i in range(N):
    for j in range(M):
        arr[i][j] = arr1[i][j] + arr2[i][j]

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()