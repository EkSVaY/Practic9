n = 1
k = 0
while n != 0:
    n = int(input())
    if ((n - 3) - 3 * ((n - 3) // 2)) % 2 == 0:
        k += 1

print(k)