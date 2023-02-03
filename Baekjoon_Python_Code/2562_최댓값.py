import sys
input = sys.stdin.readline

num = 0
num_cnt = 0
cnt = 1
while True:
    try:
        N = int(input())
        if N > num:
            num = N
            num_cnt = cnt
        cnt += 1
    except:
        break
print(num)
print(num_cnt)
        