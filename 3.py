n = int(input())
i_2 = 1
for i_1 in range(2, (n // 2) + 1):
    if n % i_1 == 0:
       if i_1 >= i_2:
           i_2 = i_1

print(int(n / i_2))
