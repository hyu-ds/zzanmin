import sys
input = sys.stdin.readline

R1, S = map(int, input().strip("\n").split())

print("%d"%(2*S-R1))