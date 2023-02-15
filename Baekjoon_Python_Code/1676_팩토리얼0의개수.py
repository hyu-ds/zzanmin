import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
for i in range(1, N+1):
    if i%5 == 0:
        while i%5 != 0:
            cnt += 1
            i = i//5
print(cnt)