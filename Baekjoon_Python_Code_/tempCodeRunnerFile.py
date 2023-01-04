N = int(input())
location = {}

for i in range(N):
    x, y = map(int, input().split(" "))
    location[x] = y

sorted_location = sorted(location.items())
minus = 0
for i in range(N):
    for j in range(i+1, N):
        if sorted_location[j][0] - sorted_location[i][0] < 10:
            if abs(sorted_location[j][1] - sorted_location[i][1]) < 10:
                minus += (10 + sorted_location[i][0] - sorted_location[j][0]) *  (10 - abs(sorted_location[i][1] - sorted_location[j][1]))
            elif sorted_location[j][0] == sorted_location[i][0]:
                if sorted_location[j][1] == sorted_location[i][1]:
                    minus += 100
                elif abs(sorted_location[j][1] - sorted_location[i][1]) < 10:
                    minus += 10 *  (10 - abs(sorted_location[i][1] - sorted_location[j][1]))
            else:        
                pass
        else:
            pass

print(100*N-minus)