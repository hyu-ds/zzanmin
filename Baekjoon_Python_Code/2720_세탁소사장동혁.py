import sys
input = sys.stdin.readline

Q = 25
D = 10
N = 5
P = 1

T = int(input())

for _ in range(T):
    C = int(input())
    q, c = divmod(C, Q)
    d, c = divmod(c, D)
    n, c = divmod(c, N)
    p, c = divmod(c, P)

    print(q, d, n, p)
