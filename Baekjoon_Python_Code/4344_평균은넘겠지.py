import sys
input = sys.stdin.readline
C = int(input())
for i in range(C):
    lst = list(map(int, input().rstrip().split()))
    score = []
    num = 0
    for j in range(1, lst[0]+1):
        score.append(lst[j])
    for k in range(lst[0]):
        if score[k] > sum(score)/lst[0]:
            num += 1
        else:
            pass
    print("%.3f"%((num/lst[0])*100)+"%")