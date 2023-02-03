import sys
input = sys.stdin.readline
lst = []
div = 0
for i in range(10):
    n = int(input())
    div = n%42
    if div in lst:
        pass
    else:
        lst.append(div)
print(len(lst))