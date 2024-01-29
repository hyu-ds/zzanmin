import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    cnt = 1
    c = {}
    for n in range(N):
        a, b = input().strip('\n').split()
        if b not in c.keys():
            c[b] = []
        c[b].append(a)

    for i in c.keys():
        cnt *= len(c[i])+1

    print(cnt-1)