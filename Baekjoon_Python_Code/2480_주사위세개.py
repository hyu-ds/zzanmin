import sys

A, B, C = map(int, sys.stdin.readline().strip('\n').split())

if A == B == C:
    print(10000+A*1000)
elif A == B or B == C:
    print(1000+B*100)
elif A == C:
    print(1000+A*100)
else:
    print(100*max(A, B, C))
