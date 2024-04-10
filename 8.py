def first():
    i_1 = ""
    for i_2 in range(1, 10):
        i_1 = i_1 + str(i_2)
        print(f"{i_1} * 8 + {i_2} = {int(i_1) * 8 + i_2}")


def second():
    i_1 = ""
    for i_2 in range(1, 10):
        i_1 = i_1 + str(i_2)
        print(f"{i_1} * 9 + {i_2 + 1} = {int(i_1) * 9 + (i_2 + 1)}")


def third():
    for i_2 in range(1, 10):
        i_1 = "1" * i_2
        print(f"{i_1} * {i_1} = {int(i_1) * int(i_1)}")


first()
print()
second()
print()
third()
