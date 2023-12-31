import sys
input = sys.stdin.readline

N, K = map(int, input().split())
measures = []

for i in range(N):
    if N%(i+1) == 0:
        measures.append(i+1)

if K > len(measures):
    print(0)
else:
    print(measures[K-1])