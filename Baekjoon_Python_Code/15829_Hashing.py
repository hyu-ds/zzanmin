import sys
input = sys.stdin.readline

L = int(input())

string = list(input().strip('\n'))

dic = {}

for i in range(ord('a'), ord('z')+1):
    dic[chr(i)] = i - ord('a') + 1

sum = 0

for idx, i in enumerate(string):
    sum += dic[i] * 31 ** idx
print(sum%1234567891)