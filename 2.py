import math

a = int(input())
if a > 2:
    while a > 2:
        a = math.sqrt(a)
        print(round(a, 3))
else:
    print("Ошибка")
