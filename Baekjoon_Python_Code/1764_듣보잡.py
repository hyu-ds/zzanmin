import sys
input = sys.stdin.readline

N, M = map(int, input().split())

L = []
S = []

for n in range(N):
    L.append(input().strip('\n'))

for m in range(M):
    S.append(input().strip('\n'))

LS = list(set(L)&set(S))

LS.sort()

print(len(LS))

for i in LS:
    print(i)