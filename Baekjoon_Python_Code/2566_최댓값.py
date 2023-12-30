import sys
input = sys.stdin.readline

arr = []

for i in range(9):
    arr.append(list(map(int, input().strip('\n').split())))

M = 0
row, col = 0, 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > M:
            M = arr[i][j]
            row, col = i, j

print(f'{M}\n{row+1} {col+1}')
