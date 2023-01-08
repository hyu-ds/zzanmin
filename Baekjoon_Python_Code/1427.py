import sys

lst = list(sys.stdin.readline().strip('\n'))
lst.sort(reverse=True)

N = map(int, lst)
print(*N, sep = '')
    