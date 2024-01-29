import sys
input = sys.stdin.readline

A = input().strip('\n')
B = input().strip('\n')

def LCS_LENGTH(X, Y):
    m = len(X)
    n = len(Y)
    b = [['_' for j in range(n+1)] for i in range(m+1)]
    c = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                b[i][j]="upperleft"
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                b[i][j]="upper"
            else:
                c[i][j]=c[i][j-1]
                b[i][j]="left"
    return c, b

def PRINT_LCS(b, X, i, j):
    if i==0 or j==0:
        return None
    if b[i][j]=="upperleft":
        PRINT_LCS(b, X, i-1, j-1)
        print(X[i-1],end='')
    elif b[i][j]=="upper":
        PRINT_LCS(b, X, i-1, j)
    else:
        PRINT_LCS(b, X, i, j-1)

c, b = LCS_LENGTH(A, B)

PRINT_LCS(b, A, len(A), len(B))