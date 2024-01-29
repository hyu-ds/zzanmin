import sys
input = sys.stdin.readline

N = int(input())

size = []

for i in range(N):
    x, y = map(int, input().split())
    size.append([x, y])

def compare(lst, target):
    x, y = target
    cnt = 1
    for i in range(len(lst)):
        X, Y = lst[i]
        if X > x and Y > y:
            cnt += 1
    return cnt

for target in size:
    print(compare(size, target), end=' ')
