import sys
input = sys.stdin.readline

N = int(input())

cnt = [0, 0, 1, 1]

for i in range(4, N+1):
    m = []
    m.append(cnt[i-1]+1)
    if i%2==0:
        m.append(cnt[i//2]+1)
    if i%3==0:
        m.append(cnt[i//3]+1)
    cnt.append(min(m))

print(cnt[N])