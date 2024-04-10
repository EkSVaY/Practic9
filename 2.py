a = 0
b = 0
f = 0
while b != -1:
    b = int(input())
    f += 1
    if b > a:
        a = b

print(f-1)
