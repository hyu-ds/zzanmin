A, B, C = map(int, input().split(' '))

if C!=B:
    Break_Even_Point = A/(C-B)

    if Break_Even_Point > 0:
        print(int(Break_Even_Point)+1)
    else:
        print(-1)
else:
    print(-1)