import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, N+1):
    A, B = input().strip("\n").split()
    print("Case #%d: %d"%(i, int(A)+int(B)))