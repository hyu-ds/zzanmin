import sys
input = sys.stdin.readline

T = int(input())
R = 0

for i in range(T):
    lst = list(input().strip("\n").split())
    for _ in lst:
        if _ == "@":
            R = R * 3
        elif _ == "%":
            R = R + 5
        elif _ == "#":
            R = R - 7
        else:
            R = float(_)
    print("%.2f"%R)