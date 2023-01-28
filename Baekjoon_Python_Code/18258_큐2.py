import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Linked_List:
    def __init__(self, data):
        self.head = Node(data)
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
    def pop(self):
        if self.head.next == None:
            print("-1")
        else:
            print(self.head)    
            self.head = self.head.next
            return

def push(que, X):
    que.append(X)
def pop(que):
    print(que.pop())
def size(que):
    print(len(que))
def empty(que):
    if len(que) == 0:
        print("1")
    else:
        print("0")
def front(que):
    if len(que) == 0:
        print("-1")
    else:
        print(que[0])
def back(que):
    if len(que) == 0:
        print("-1")
    else:
        print(que[-1])

N = int(sys.stdin.readline())
que = Linked_List()
for i in range(N):
    commend = sys.stdin.readline().strip("\n")
    if "push" in commend:
        push(que, int(commend.split()[-1]))
    elif "pop" in commend:
        if len(que) == 0:
            print("-1")
        else:
            pop(que)
            que = que[1:]
    elif "front" in commend:
        front(que)
    elif "back" in commend:
        back(que)
    elif "empty" in commend:
        empty(que)
    else:
        size(que)