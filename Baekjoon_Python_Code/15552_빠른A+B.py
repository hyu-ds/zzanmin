import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    A, B = input().strip("\n").split()
    print("%d"%(int(A)+int(B)))