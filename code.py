def decimal_to_binary(num):
    while num > 0:
        l = []
        p = []
        a = num % 2
        b = num / 2
        l.append(a)
        p.append(b)
    return l