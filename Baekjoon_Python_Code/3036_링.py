import sys
input = sys.stdin.readline
def GCD(a, b):
    if a%b != 0:
        c = a%b
        return GCD(b, c)
    else:
        return b
N = int(input())
r = list(map(int, input().rstrip().split()))
for i in range(1, N):
    gcd = GCD(r[0], r[i])
    print(int(r[0]/gcd), end='')
    print("/", end='')
    print(int(r[i]/gcd))
