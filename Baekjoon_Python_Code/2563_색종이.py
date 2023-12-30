import sys
input = sys.stdin.readline

arr = [[0 for j in range(100)] for i in range(100)]

n = int(input())

for k in range(n):
    b, h = map(int, input().strip('\n').split())
    for i in range(99-h-10, 99-h):
        for j in range(b, b+10):
            arr[i][j] = 1

s = 0

for i in range(100):
    for j in range(100):
        s += arr[i][j]

print(s)
