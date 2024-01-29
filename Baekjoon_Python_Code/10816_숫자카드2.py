import sys
input = sys.stdin.readline

N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))

M_origin = M_lst.copy()

M_lst.sort()

def binary(A:list, n, left, right):
    if left > right:
        return 0
    
    mid = round((left+right)/2)

    if A[mid] == n:
        return 1
    elif A[mid] < n:
        return binary(A, n, mid+1, right)
    elif A[mid] > n:
        return binary(A, n, left, mid-1)

dic = {}

for i in range(N):
    dic[N_lst[i]] = 0

for i in range(M):
    dic[M_lst[i]] = 0

for i in range(N):
    dic[N_lst[i]] += binary(M_lst, N_lst[i], 0, M-1)

for i in M_origin:
    print(dic[i], end=' ')