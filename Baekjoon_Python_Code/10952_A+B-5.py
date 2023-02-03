import sys
input = sys.stdin.readline

while True:
    A, B = map(int, input().strip("\n").split())
    if A == B == 0:
        break 
    print("%d"%(A+B))