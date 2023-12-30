import sys
input = sys.stdin.readline

dgr = {'A+':4.5,
       'A0':4.0,
       'B+':3.5,
       'B0':3.0,
       'C+':2.5,
       'C0':2.0,
       'D+':1.5,
       'D0':1.0,
       'F':0.0,
       'P':0.0}

total_cnt = 0.0
total_score = 0.0

for _ in range(20):
    info = list(input().strip('\n').split())
    if info[2] == 'P':
        info[1] = 0.0
    hour = float(info[1])
    score = dgr[info[2]]
    total_cnt += hour
    total_score += hour*score

print(total_score/total_cnt)

