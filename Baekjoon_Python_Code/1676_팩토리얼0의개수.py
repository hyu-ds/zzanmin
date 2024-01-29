import sys
input = sys.stdin.readline

N = int(input())

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

f = factorial(N)

fr = str(f)[::-1]

cnt = 0
number = 0

while number == 0:
    number = int(fr[cnt])
    cnt += 1

print(cnt-1)