import sys

A, B = map(int, sys.stdin.readline().strip('\n').split())
C = int(sys.stdin.readline())
D = B+C

while D >= 60:
    D -= 60
    A += 1

if A >= 24:
    print('%d %d'%(A-24, D))
else:
    print('%d %d'%(A, D))
