amount = 0
cels = float(input())
while cels != 0:
    last_cels = cels
    cels = float(input())
    if last_cels > cels:
        amount += 1

print(amount - 1)
