import sys

def check(stack, A, B, C):
    if isempty(stack):
        pass    
    else:
        if stack[-1] == "(":
            A += 1
            stack.pop()
        else:
            B += 1
            stack.pop()
        return A, B, C

def isempty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

T = int(sys.stdin.readline())

for i in range(T):
    PS = list(sys.stdin.readline().strip('\n'))
    A_ = 0
    B_ = 0
    isVPS = False
    for j in range(len(PS)):
        A = 0
        B = 0
        C = False
        returnvalues = check(PS, A, B, C)
        A_ += int(returnvalues[0])
        B_ += int(returnvalues[1])
    if A_ == B_:
        isVPS = True
    if isVPS:
        print("YES")
    else:
        print("NO")