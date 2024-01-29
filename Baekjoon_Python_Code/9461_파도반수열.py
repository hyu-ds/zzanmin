import sys
input = sys.stdin.readline

T = int(input())

P = [0, 1, 1, 1, 2, 2]

for n in range(6, 101):
    P.append(P[n-1] + P[n-5])

for t in range(T):
    print(P[int(input())])