import math

while True:
    num = int(input("Введите число: "))
    if math.sqrt(num) % 1 == 0:
        print("Поздравляю! Чисто является полным квадратом!")
        break
    print("Число не ялвяется полным квадратом!")
