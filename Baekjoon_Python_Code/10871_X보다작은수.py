import sys

N, X = map(int, sys.stdin.readline().strip('\n').split())
A = list(map(int, sys.stdin.readline().strip('\n').split()))
Ans = []
for i in range(N):
    if A[i] < X:
        Ans.append(A[i])
    else:
        pass
for i in range(len(Ans)):
    print(Ans[i], end=" ")
