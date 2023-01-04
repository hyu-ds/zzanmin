Initial_value = [1, 1, 2, 2, 2, 8]
Test_value = list(map(int, input().split(" ")))

for i in range(5):
    print(Initial_value[i]-Test_value[i], end=" ")
print(Initial_value[5]-Test_value[5])