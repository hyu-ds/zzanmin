import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

A.sort()

def binary(A, n, left, right):
    if left > right:
        return 0

    mid = round((left+right)/2)

    if n > A[mid]:
        return binary(A, n, mid+1, right)
    elif n < A[mid]:
        return binary(A, n, left, mid-1)
    elif n == A[mid]:
        return 1

        
for i in B:
    print(binary(A, i, 0, N-1))


## 이진탐색 알고리즘


    