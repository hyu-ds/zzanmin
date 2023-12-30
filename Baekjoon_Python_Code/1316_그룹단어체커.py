import sys
input = sys.stdin.readline

def isGroup(s:list):
    unique = []
    prev = None
    for i in s:
        if i != prev and i in unique:
            return 0
        elif i != prev and i not in unique:
            unique.append(i)
        else:
            pass
        prev = i
    return 1

n = int(input())

cnt = 0

for i in range(n):
    cnt += isGroup(list(input().strip('\n')))

print(cnt)