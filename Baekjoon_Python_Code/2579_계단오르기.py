import sys
input = sys.stdin.readline

score = [0]

N = int(input())

for i in range(N):
    score.append(int(input()))

dpscore = [0 for i in range(N+1)]

for i in range(1, N+1):
    if i == 1:
        dpscore[i] = score[i]
    elif i == 2:
        dpscore[i] = score[i] + dpscore[i-1]
    else:
        dpscore[i] = score[i] + max(score[i-1]+dpscore[i-3], dpscore[i-2])

print(dpscore[N])