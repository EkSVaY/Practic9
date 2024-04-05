answer = False
n = int(input())
while n > 1:
    n /= 2
    if n == 1:
        answer = True

if answer:
    print("Верно")
else:
    print("Неверно")
