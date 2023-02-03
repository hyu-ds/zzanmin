import sys
input = sys.stdin.readline

# N = int(input())
# num_lst = list(map(int, input().rstrip().split()))
# print("%d %d"%(min(num_lst), max(num_lst)))
# 위 코드는 파이썬의 max함수와 min함수를 이용해 풀었다.
# 아래의 코드는 정렬을 하여 출력해 본 것이다.

N = int(input())
num_lst = list(map(int, input().rstrip().split()))
num_lst.sort()
print("%d %d"%(num_lst[0], num_lst[-1]))

# 시간초과를 예상했는데 그런 일은 일어나지 않았다.
# 정렬 단계에서 정렬의 시간초과에 대해 더 자세히 다룰 수 있을 것 같다.