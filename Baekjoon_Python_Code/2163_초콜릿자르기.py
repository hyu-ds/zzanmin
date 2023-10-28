import sys
input = sys.stdin.readline

N, M = map(int, input().strip("\n").split())

def Div(N, M):
    if N == 1 or M == 1:
        if N == 1 and M == 1:
            return 0
        elif N == 1 and M > 1:
            return M - 1
        elif N > 1 and M == 1:
            return N - 1
    if N > 1 and M > 1:
        return 1 + Div(N, 1) + Div(N, M-1)
    
print(Div(N, M))