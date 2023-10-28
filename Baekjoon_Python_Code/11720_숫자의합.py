import sys
input = sys.stdin.readline

N = int(input())

numstr = input().strip("\n")
numlst = [int(numstr[i]) for i in range(N)]
print(sum(numlst))
