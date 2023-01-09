import sys

N, n = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().strip('\n').split()))
lst.sort()
print(lst[N-n])