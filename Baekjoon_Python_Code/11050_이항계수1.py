import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
def factorials(a):
    result = 1
    for item in range(1, a+1):
        result *= item
    return result
A = factorials(N)
B = factorials(K)
C = factorials(N-K)
print(int(A/(B*C)))