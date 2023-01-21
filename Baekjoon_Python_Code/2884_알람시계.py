import sys
H, M = map(int, sys.stdin.readline().strip('\n').split())

def Time(H, M):
    if M >= 45:
        print('%d %d'%(H, M-45))
    else:
        if H == 0:
            print('%d %d'%(23, M+15))
        else:
            print('%d %d'%(H-1, M+15))

Time(H, M)