import sys
input = sys.stdin.readline

s = list(input().strip('\n').upper())
s_unique = set(s)

Max_num = 0 
Max_alpha = None
flag = False

for i in s_unique:
    if s.count(i) > Max_num:
        Max_alpha = i
        Max_num = s.count(i)
        flag = False
    elif s.count(i) == Max_num:
        flag = True

if flag:
    print("?")
else:
    print(Max_alpha)

