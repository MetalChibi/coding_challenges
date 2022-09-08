# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    x = []
    binary = str(bin(N)[2:]).split("1")
    for i in binary[:-1]:
        if '0' in i:
            x.append(len(i))

    if not x:
        return 0
    else:
        return max(x)



print(solution(6291457))