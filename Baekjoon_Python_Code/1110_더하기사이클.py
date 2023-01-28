import sys
input = sys.stdin.readline

N = int(input())
N_next = 0
N_temp = N
cnt = 0
while True:
    if N > 10:
        if N//10+N%10 > 10:
            N_next = (N%10)*10 + (N//10+N%10)%10
        elif N//10+N%10 == 10:
            N_next = (N%10)*10
        else:
            N_next = (N%10)*10 + N//10+N%10
    else:
        N_next = (N%10)*10 + N//10+N%10
    cnt += 1
    N = N_next
    if N_temp == N_next:
        break
print(cnt)