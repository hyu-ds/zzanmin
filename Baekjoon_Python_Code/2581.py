M = int(input())
N = int(input())

prime_Num = []

for i in range(2, 10000):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_Num.append(i)

PN = []

for i in range(len(prime_Num)):
    if M <= prime_Num[i] <=N:
        PN.append(prime_Num[i])
if len(PN) == 0:
    print(-1)
else:
    print(sum(PN))
    print(min(PN))


    