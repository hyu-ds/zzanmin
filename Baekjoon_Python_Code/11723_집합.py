import sys
input = sys.stdin.readline

class SET():
    def __init__(self):
        self.S = []

    def add(self, x):
        s = set([x])
        self.S = set(self.S).union(s)

    def remove(self, x):
        s = set([x])
        if len(self.S) != 0:
            self.S = self.S - s
    
    def check(self, x):
        if x in self.S:
            return 1
        else:
            return 0
        
    def toggle(self, x):
        if x in self.S:
            self.remove(x)
        else:
            self.add(x)

    def all(self):
        self.S = set([i for i in range(1, 21)])

    def empty(self):
        self.S = {}

M = int(input())

S = SET()

for m in range(M):
    command = list(input().strip('\n').split())

    if command[0] == 'add':
        S.add(int(command[1]))

    elif command[0] == 'remove':
        S.remove(int(command[1]))

    elif command[0] == 'check':
        print(S.check(int(command[1])))

    elif command[0] == 'toggle':
        S.toggle(int(command[1]))

    elif command[0] == 'all':
        S.all()

    elif command[0] == 'empty':
        S.empty()
