import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin =[]

for i in range(N):
    coin.append(int(input()))

cnt = 0

coin.sort(reverse=True)

for i in coin:
    if K >= i:
        cnt += K//i
        K = K%i

print(cnt)