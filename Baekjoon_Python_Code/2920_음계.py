import sys
input = sys.stdin.readline

asc = [1, 2, 3, 4, 5, 6, 7, 8]
desc = [8, 7, 6, 5, 4, 3, 2, 1]

N = list(map(int, input().split()))

if N == asc:
    print('ascending')
elif N == desc:
    print('descending')
else:
    print('mixed')