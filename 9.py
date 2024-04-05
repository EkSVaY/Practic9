n, k, r = map(int, input().split(" "))
process = 1 + (k / 100)
days = 1

while n <= r:
    n *= process
    days += 1

print(days)
