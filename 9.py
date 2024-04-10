a = int(input())
for a in range(2, a + 1):
    k = 0
    for i in range(2, a):
        if a % i == 0:
            k += 1
    if k == 0:
        print(a, k)
