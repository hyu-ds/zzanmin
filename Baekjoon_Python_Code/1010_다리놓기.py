import sys
input = sys.stdin.readline
T = int(input())
def factorials(a):
    result = 1
    for item in range(1, a+1):
        result *= item
    return result
for i in range(T):
    N, M = map(int, input().rstrip().split())
    A = factorials(M)
    B = factorials(N)
    C = factorials(M-N)
    print(int(A/(B*C)))