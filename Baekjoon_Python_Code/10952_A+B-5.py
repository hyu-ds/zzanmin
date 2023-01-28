import sys
input = sys.stdin.readline

while True:
    A, B = input().strip("\n").split()
    if int(A) == int(B) == 0:
        break 
    print("%d"%(int(A)+int(B)))