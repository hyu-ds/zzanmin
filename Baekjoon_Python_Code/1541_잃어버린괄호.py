import sys
input = sys.stdin.readline

lst = list(input().strip('\n').split('-'))

s = 0

cnt = 0

for i in lst:
    if cnt == 0: 
        s += sum(list(map(int, i.split('+'))))
        cnt += 1
    else:
        s -= sum(list(map(int, i.split('+'))))

print(s)


