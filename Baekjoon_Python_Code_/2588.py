A = int(input())
B = int(input())

line_1 = A*(B%10)
line_2 = A*((B%100)//10)
line_3 = A*(B//100)
print("%d\n%d\n%d\n%d"%(line_1, line_2, line_3, 100*line_3 + 10*line_2 + line_1))