import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nameTonumber = {}
numberToname = {}

for idx in range(1, N+1):
    name = input().strip('\n')
    nameTonumber[name] = str(idx)
    numberToname[str(idx)] = name

for m in range(M):
    question = input().strip('\n')
    try:
        print(nameTonumber[question])
    except:
        print(numberToname[question])