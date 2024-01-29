import sys
input = sys.stdin.readline

N = int(input())

P = list(map(int, input().split()))

P.sort()

time = [0 for i in range(len(P)+1)]

for i in range(1, len(P)+1):
    time[i] = time[i-1] + P[i-1]

print(sum(time))