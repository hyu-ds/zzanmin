import sys
import heapq
input = sys.stdin.readline

heap = []

heapq.heappush(heap, 1)
print(heapq.heappop(heap))