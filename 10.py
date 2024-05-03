def layers(k, n_f):
    ls = 0
    if n_f == 0:
        return ls + 1
    elif k < n_f:
        for i in range(k + 1, n_f + 1):
            ls += layers(i, n_f - i)
        return ls
    else:
        return ls


n = int(input())
print(layers(0, n))
