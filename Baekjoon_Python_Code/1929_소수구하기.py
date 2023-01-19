import sys

M, N = map(int, sys.stdin.readline().strip('\n').split())
arr = [False, False] + [True] * (N-1)
prime = []
for i in range(2, N+1):
    if arr[i]:
        prime.append(i)
    for j in range(2*i, N+1, i):
            arr[j] = False
for i in range(len(prime)):
    if prime[i] >= M:
        print(prime[i])
