""" import sys

N = int(sys.stdin.readline())
lst = []
for i in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)
for i in range(N):
    print(lst[i]) """

## sort 함수를 사용하면 메모리 초과가 발생함