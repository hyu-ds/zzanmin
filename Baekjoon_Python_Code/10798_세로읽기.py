import sys
input = sys.stdin.readline

arr = [['_' for j in range(15)] for i in range(5)]

for i in range(5):
    lst = list(input().strip('\n'))
    for j in range(len(lst)):
        arr[i][j] = lst[j]

for j in range(15):
    for i in range(5):
        if arr[i][j] == '_':
            print('', end='')
        else:
            print(arr[i][j], end='')