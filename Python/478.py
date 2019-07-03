import sys
from math import sqrt

counter = 0
shapes = []


def form(x1, y1, x2, y2, x3, y3, x, y) -> bool:
    if x2 - x1 != 0:
        K = (y2 - y1) / (x2 - x1)
        C1 = y1 - ((y2 - y1) / (x2 - x1)) * x1
        C2 = y3 - K * x3
    else:
        return x1 > x > x3 or x1 < x < x3
    return C1 < y - K * x < C2 or C1 > y - K * x > C2


def is_inside(x1, y1, x2, y2, x3, y3, x, y):
    return form(x1, y1, x2, y2, x3, y3, x, y) and form(x2, y2, x3, y3, x1, y1, x, y) and form(x3, y3, x1, y1, x2, y2, x, y)


def is_in_triangle(cords, x, y):
    if is_inside(cords[1], cords[2], cords[3], cords[4], cords[5], cords[6], x, y):
        global contained
        contained = True
        print(f"Point {counter} is contained in figure {cords[-1]}")


def is_in_rectangle(cords: list, x: float, y: float):
    if cords[1] < x < cords[3] and cords[2] > y > cords[4]:
        global contained
        contained = True
        print(f"Point {counter} is contained in figure {cords[-1]}")


def is_in_circule(cords, x, y):
    if sqrt((x - cords[1])**2 + (y - cords[2])**2) < cords[3]:
        global contained
        contained = True
        print(f"Point {counter} is contained in figure {cords[-1]}")


def print_figures(x: float, y: float):
    for shape in shapes:
        if shape[0] == "t":
            is_in_triangle(shape, x, y)
        elif shape[0] == "c":
            is_in_circule(shape, x, y)
        elif shape[0] == "r":
            is_in_rectangle(shape, x, y)


if "_main_" == '__name__':
    figure = 0
    for line in sys.stdin:
        if line.strip() == "*":
            break
        figure += 1
        shape = [line[0]]
        shape = shape + list(map(float, line[2:].split()))
        shape.append(figure)

        shapes.append(shape)

    contained = False
    for line in sys.stdin:
        contained = False
        cords = list(map(float, line.split()))
        if cords[0] == 9999.9 and cords[1] == 9999.9:
            break
        counter += 1
        print_figures(cords[0], cords[1])
        if not contained:
            print(f"Point {counter} is not contained in any figure")