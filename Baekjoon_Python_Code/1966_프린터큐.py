import sys
input = sys.stdin.readline

from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque([])
    
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if len(self.size()) == 0:
            return True
        else:
            return False

    def push(self, x):
        self.queue.append(x)
    
    def findMax(self):
        M = self.queue[0][1]
        for i in range(1, self.size()):
            if M < self.queue[i][1]:
                return True
        return False
    
    def print(self, n):
        cnt = 1
        while True:
            if self.findMax():
                self.queue.append(self.queue.popleft())
            else:
                if self.queue[0][0]==n:
                    return cnt
                self.queue.popleft()
                cnt+=1
    
T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))

    q = Queue()

    for idx, i in enumerate(W):
        q.push([idx, i])

    cnt = q.print(M)

    print(cnt)