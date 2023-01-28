# try와 except을 배울 수 있는 기본적인 문제

import sys
input = sys.stdin.readline

while True:
    try:
        A, B = map(int, input().strip("\n").split())
        print("%d"%(A+B))
    except:
        break
        # 또는 exit()