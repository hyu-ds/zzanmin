import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

accumulate = [0 for i in range(N+1)]

for i in range(1, N+1):
    accumulate[i] = numbers[i-1] + accumulate[i-1]

for m in range(M):
    start, end = map(int, input().split())
    print(accumulate[end]-accumulate[start-1])