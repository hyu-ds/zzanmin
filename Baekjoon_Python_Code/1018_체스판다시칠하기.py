import sys
input = sys.stdin.readline

N, M = map(int, input().split())

wboard = []
bboard = []

for n in range(N):
    lst = list(input().strip('\n'))
    wboard.append(lst.copy())
    bboard.append(lst.copy())

def toNumber(N, M, board:list, color):
    col = color
    row = color

    for i in range(N):
        for j in range(M):
            if col == board[i][j]:
                board[i][j] = 0
                if col == "B":
                    col = "W"
                else:
                    col = "B"
            else:
                board[i][j] = 1
                if col == "B":
                    col = "W"
                else:
                    col = "B"
        if row == "B":
            row = "W"
        else:
            row = "B"
        col = row
    return board

w = toNumber(N, M, wboard, "W")
b = toNumber(N, M, bboard, "B")

def count(N, M, board:list):
    m = 64

    k, l = 0, 0

    while True:
        cnt = 0
        for i in range(k, k+8):
            for j in range(l, l+8):
                cnt += board[i][j]

        if cnt < m:
            m = cnt
        if l <= M-8:
            l += 1
        if l > M-8:
            k += 1
            l = 0
        if k > N-8:
            break

    return m

wm = count(N, M, wboard)
bm = count(N, M , bboard)

if wm > bm:
    print(bm)
else:
    print(wm)