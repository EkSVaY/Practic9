n = int(input())
a = 0

while (a + 1) ** 3 <= n:
    a += 1
    print(a ** 3, end=" ")
