import sys

M, N = map(int, sys.stdin.readline().strip('\n').split())

for i in range(2, N):
    isprime = True
    for j in range(2, i):
        if i % j == 0:
            isprime = False
            break
        else:
            continue
    if (i >= M) and isprime:
        print(i)