import sys

lst = []
for i in range(5):
    num = int(sys.stdin.readline())
    lst.append(num)
lst.sort()
print(int(sum(lst)/5))
print(lst[2])