## 유클리드 호제법
import sys
input = sys.stdin.readline
A, B = map(int, input().rstrip().split())
def U(a, b):
    if a%b == 0:
        return b
    else:
        a=a%b
        return U(b, a)
Mf = int(U(A, B))
mm = int(Mf * (A/Mf) * (B/Mf))
print(Mf)
print(mm)

