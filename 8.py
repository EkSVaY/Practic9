x = int(input())
k = 0
for a in range(1, x):
    for b in range(1, x):
        if a ** 2 + b ** 2 == x:
            k += 1
print(k // 2)
