n = int(input())
s = 0
while s <= n:
    for p in range(2, n):
        summa = 0
        s = (2 ** (p - 1)) * ((2 ** p) - 1)
        if s > n:
            break
        for i in range(1, (s // 2) + 1):
            if s % i == 0:
                summa += i
        if summa == s:
            print(s)
