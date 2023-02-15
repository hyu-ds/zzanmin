import sys
input = sys.stdin.readline
A = 1
B = 1
while A != 0 and B != 0:
    A, B = map(int, input().strip("\n").split())
    if A < B:
        if B % A == 0:
            print("factor")
        else:
            print("neither")
    elif A > B:
        if A % B == 0:
            print("multiple")
        else:
            print("neither")