import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().rstrip().split()))
print(sum(lst)*100/(N*max(lst)))