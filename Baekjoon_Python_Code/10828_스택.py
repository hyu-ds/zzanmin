import sys
def checkcommend(stack, commend, number):
    if commend == "push":
        push(stack, number)
    elif commend == "pop":
        pop(stack)
    elif commend == "top":
        top(stack)
    elif commend == "size":
        size(stack)
    else:
        if isempty(stack):
            print("1")
        else:
            print("0")

def push(stack, n):
    stack.append(n)
    return stack
def pop(stack):
    if isempty(stack):
        print("-1")
    else:
        print(stack[-1])
        stack.pop()
    return stack
def top(stack):
    if isempty(stack):
        print("-1")
    else:
        print(stack[-1])
    return stack
def size(stack):
    print(len(stack))
def isempty(stack):
    empty = False
    if len(stack) == 0:
        empty = True
    return empty

N = int(sys.stdin.readline())
stack = []
for i in range(N):
    commend = sys.stdin.readline().strip("\n")
    number = None
    if "push" in commend:
        comlist = commend.split()
        commend = comlist[0]
        number = int(comlist[1])
    checkcommend(stack, commend, number)
