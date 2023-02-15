# Fraction 함수는 Fraction(a, b)를 b분의 a로 만들어주는 함수
# 이를 사용해야 부동소수점으로 인한 오차로 발생하는 틀렸습니다를 방지할 수 있음

import sys
from fractions import Fraction
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
R = Fraction(A, (B*C))
print(int(R)%10007)