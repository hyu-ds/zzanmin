import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    S = input().strip("\n")
    a, b = S[0], S[-1]
    print(a+b)