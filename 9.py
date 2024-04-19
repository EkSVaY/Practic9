n = int(input())
summa = 0
for a in range(n + 1):
    for b in range(n + 1):
        if a == b:
            summa += 2 * (a + b)
        else:
            summa += a + b

print(summa // 2)
