word = input()
s = ""

for i in range(len(word)):
    if (i + 1) % 3 == 0:
        s += word[i]

print(s)