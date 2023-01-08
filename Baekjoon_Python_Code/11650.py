import sys

N = int(sys.stdin.readline())
numlst = []

for i in range(N):
    numlst.append(list(map(int, sys.stdin.readline().split(' '))))

for i in range(len(numlst)):
    temp = numlst[i][1]
    numlst[i][1] = numlst[i][0]
    numlst[i][0] = temp

numlst.sort()

for i in range(len(numlst)):
    temp = numlst[i][0]
    numlst[i][0] = numlst[i][1]
    numlst[i][1] = temp

for i in range(len(numlst)):
    print(numlst[i][0], numlst[i][1])