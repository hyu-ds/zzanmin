import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip('\n').split(' ')))
v = int(sys.stdin.readline())
count = 0
for i in range(N):
    if arr[i] == v:
        count += 1
    else:
        pass
print(count)