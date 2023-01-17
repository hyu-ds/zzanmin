import sys

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)

N = int(sys.stdin.readline())
print(2**N-1)
hanoi(N, 1, 2, 3)
