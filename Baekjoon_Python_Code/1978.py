prime = []
for i in range(2, 1000):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)

N = int(input())
Num_list = list(map(int, input().split(" ")))
Num_of_Prime = 0

for i in range(N):
    if Num_list[i] in prime:
        Num_of_Prime += 1
    else:
        continue
print(Num_of_Prime)