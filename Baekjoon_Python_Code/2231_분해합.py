import sys
input = sys.stdin.readline

def disassemble(n):
    number = n
    numbers = sum(list(map(int, str(n))))

    return number + numbers

N = int(input())

flag = True

n = N - len(str(N))*9

if n < 0:
    n = 1

while n < N:
    if N == disassemble(n):
        print(n)
        flag = False
        break
    n += 1

if flag:
    print(0)