for send in range(1000, 10000):
    for more in range(1000, 10000):
        money = send + more
        if money // 10000 == more // 1000 and (money // 1000) % 10 == (more // 100) % 10 \
            and (money // 100) % 10 and (send // 10) % 10 and (money // 10) % 10 == (more % 10) and \
                (send // 100) % 10 == (more % 10):
            print(send, more, money)
