for ab in range(10, 100):
    proizv = ab * ab
    if proizv % 100 == ab and proizv // 1000 == 0:
        print(proizv)
