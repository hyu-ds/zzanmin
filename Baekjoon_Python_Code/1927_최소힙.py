import sys
import heapq
input = sys.stdin.readline

heap = []

N = int(input())

for n in range(N):
    x = int(input())
    if x == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, x)
        # heapq.heapify(heap)