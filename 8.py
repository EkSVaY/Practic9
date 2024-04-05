n = int(input())
try_pop = 0
while n > 1:
    n /= 2
    try_pop += 1

print(try_pop)