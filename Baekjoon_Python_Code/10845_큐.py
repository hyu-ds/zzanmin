import sys
input = sys.stdin.readline

from collections import deque

class queue():
    def __init__(self):
        self.q = deque([])

    def size(self):
        return len(self.q)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
        
    def front(self):
        if self.size() == 0:
            return -1
        return self.q[0]
    
    def back(self):
        if self.size() == 0:
            return -1
        return self.q[-1]
    
    def push(self, x):
        self.q.append(x)
    
    def pop(self):
        if self.size() == 0:
            return -1
        return self.q.popleft()

N = int(input())

q = queue()

for i in range(N):
    inPut = list(input().split())

    if len(inPut) == 2:
        commend, num = inPut
    else:
        commend = inPut[0]

    if commend == 'push':
        q.push(int(num))

    elif commend == 'pop':
        print(q.pop())
    
    elif commend == 'front':
        print(q.front())

    elif commend == 'back':
        print(q.back())

    elif commend == 'empty':
        print(q.empty())
    
    elif commend == 'size':
        print(q.size())