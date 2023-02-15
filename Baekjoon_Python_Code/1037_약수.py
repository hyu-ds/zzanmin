import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().strip("\n").split()))
if N == 1:
    print(num_list[0]**2)
else:
    print(max(num_list)*min(num_list))
    
