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
    
    def PUSHfront(self, x):
        self.q.appendleft(x)

    def PUSHback(self, x):
        self.q.append(x)
    
    def POPfront(self):
        if self.size() == 0:
            return -1
        return self.q.popleft()
    
    def POPback(self):
        if self.size() == 0:
            return -1
        return self.q.pop()
    
N = int(input())

q = queue()

for i in range(N):
    inPut = list(input().split())

    if len(inPut) == 2:
        commend, num = inPut
    else:
        commend = inPut[0]

    if commend == 'push_front':
        q.PUSHfront(int(num))

    elif commend == 'push_back':
        q.PUSHback(int(num))

    elif commend == 'pop_front':
        print(q.POPfront())

    elif commend == 'pop_back':
        print(q.POPback())
    
    elif commend == 'front':
        print(q.front())

    elif commend == 'back':
        print(q.back())

    elif commend == 'empty':
        print(q.empty())
    
    elif commend == 'size':
        print(q.size())