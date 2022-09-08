def binary_gaps(N):
    x = []
    binary = str(bin(N)[2:]).split("1")
    for i in binary[:-1]:
        if '0' in i:
            x.append(len(i))

    if not x:
        return 0
    else:
        return max(x)


print(binary_gaps(6291457))
