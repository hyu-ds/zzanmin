# 1. OX를 분리해서 리스트로 만들 필요 없이 j in list를 사용하면 된다.
# 2. score를 사용해서 점수를 누적하고, 합산은 따로 구한다.

import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    sum_score = 0
    score = 0
    OX_lst = input().rstrip()
    for j in OX_lst:
        if j == "O":
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)