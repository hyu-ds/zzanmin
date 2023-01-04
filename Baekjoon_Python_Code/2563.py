N = int(input())
location = {}

for i in range(N):
    x, y = map(int, input().split(" "))
    location[x] = y

sorted_location = sorted(location.items())
minus = 0

if len(sorted_location) == N:
    for i in range(N):
        for j in range(i+1, N):
            if sorted_location[j][0] - sorted_location[i][0] < 10:
                if abs(sorted_location[j][1] - sorted_location[i][1]) < 10:
                    minus += (10 + sorted_location[i][0] - sorted_location[j][0]) *  (10 - abs(sorted_location[i][1] - sorted_location[j][1]))
                else:
                    pass
    print(100*N-minus)

else:
    for i in range(len(sorted_location)):
        for j in range(i+1, len(sorted_location)):
            if sorted_location[j][0] - sorted_location[i][0] < 10:
                if abs(sorted_location[j][1] - sorted_location[i][1]) < 10:
                    minus += (10 + sorted_location[i][0] - sorted_location[j][0]) *  (10 - abs(sorted_location[i][1] - sorted_location[j][1]))
                else:
                    pass   
    print(100*len(sorted_location)-minus) 
            

