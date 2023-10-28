import sys
input = sys.stdin.readline

def basket(a, b, lst):
    lst0 = lst[0:a]
    lst1 = lst[a:b]
    lst2 = lst[b:]

    return lst0+lst1[::-1]+lst2

N, M = map(int, input().strip("\n").split())

lst = [i+1 for i in range(N)]

for i in range(M):
    a, b = map(int, input().strip("\n").split())
    lst = basket(a-1, b, lst)

print(*lst)



