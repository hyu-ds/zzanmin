import sys
input = sys.stdin.readline

A, B, C = map(int, input().strip("\n").split())

numlist = [A, B, C]

numlist.sort()

print(numlist[1])