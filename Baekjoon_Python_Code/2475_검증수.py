import sys
input = sys.stdin.readline

u = list(map(int,input().strip('\n').split()))

n = 0

for i in u:
    n += i**2

print(int(n%10))