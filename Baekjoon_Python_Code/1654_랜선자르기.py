import sys
input = sys.stdin.readline

K, N = map(int, input().split())

length = [int(input()) for i in range(K)]

low = 1
high = max(length)

while low <= high:
    cnt = 0
    mid = (high+low)//2
    for i in length:
        cnt += i//mid
    if cnt < N:
        low = low
        high = mid-1
    elif cnt >= N:
        low = mid+1
        high = high

print(high)