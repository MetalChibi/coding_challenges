# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, colors):
    # write your code in Python 3.6
    # abs()
    smallest = 0
    red = []
    green = []

    coords = [[x, y] for x, y in zip(X, Y)]
    for color, coord in zip(list(colors), coords):
        if color == 'R':
            red.append(coord)
        else:
            green.append(coord)

    if len(red) <= len(green):
        smallest = len(red)
    else:
        smallest = len(green)

    min_red = []
    min_green = []

    for i in range(0, smallest):
        min_red.append(min(red))
        red.remove(min(red))
        min_green.append(min(green))
        green.remove(min(green))

    print(min_red, min_green)

    return len(min_red) + len(min_green)


solution([4, 0, 2, -2], [4, 1, 2, -3], "RGRR")
solution([1, 0, 0], [0, 1, -1], "GGR")
solution([5, -5, 5], [1, -1, 3], "GRG")
solution([3000, -3000, 4100, -4100, -3000], [5000, -5000, 4100, -4100, 5000], "RRGRG")
