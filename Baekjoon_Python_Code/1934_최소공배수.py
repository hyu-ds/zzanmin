## 유클리드 호제법
import sys
input = sys.stdin.readline
def U(a, b):
    if a%b == 0:
        return b
    else:
        a=a%b
        return U(b, a)
T = int(input())
for i in range(T):
    A, B = map(int, input().rstrip().split())
    Mf = int(U(A, B))
    mm = int(Mf * (A/Mf) * (B/Mf))
    print(mm)