import sys
input = sys.stdin.readline

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

s = input().strip("\n")

for i in croatia:
    s = s.replace(i, '*')

print(len(s))