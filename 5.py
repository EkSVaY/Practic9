for i in range(999999 + 1):
    if i % 10 == (i // 10000) % 10 and (i // 10) % 10 == (i // 1000) % 10:
        if (i + 1) % 10 == ((i + 1) // 10000) % 10 and ((i + 1) // 10) % 10 == ((i + 1) // 1000) % 10:
            if ((i + 2) // 10) % 10 == ((i + 2) // 10000) % 10 and ((i + 2) // 100) % 10 == ((i + 2) // 1000) % 10:
                if (i + 3) % 10 == (i + 3) // 100000 and ((i + 3) // 10) % 10 == ((i + 3) // 10000) % 10 and \
                        ((i + 3) // 100) % 10 == ((i + 3) // 1000) % 10:
                    print("Ответ:", i)
