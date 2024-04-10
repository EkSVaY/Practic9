n = int(input())

for i_1 in range(1, n):
    summa = 0
    for i_2 in range(1, i_1):
        if i_1 % i_2 == 0:
            summa += i_2
    if summa == i_1:
        print(i_1)