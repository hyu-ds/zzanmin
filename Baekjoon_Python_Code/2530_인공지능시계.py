import sys
input = sys.stdin.readline

h, m, s = map(int, input().strip("\n").split())
t = int(input())

t_s = t%60
t_m = (t//60)%60
t_h = (t//60)//60

h = h + t_h
m = m + t_m
s = s + t_s

while s >= 60 or m >= 60 or h >= 24:
    if s >= 60:
        s = s - 60
        m = m + 1

    if m >= 60:
        m = m - 60
        h = h + 1

    if h >= 24:
        h = h - 24

print("%d %d %d"%(h,m,s))
