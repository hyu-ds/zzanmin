import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    P = ""
    R, S = map(str, input().strip("\n").split())
    for _ in S:
        P = P+int(R)*_
    print(P)
