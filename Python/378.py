
def lines_intersecting(test_cases):
    print("INTERSECTING LINES OUTPUT")
    for i in range(test_cases):
        is_parallel_1 = False
        is_parallel_2 = False
        line_cordinates = input().strip().split(" ")

        x1 = int(line_cordinates[0])
        y1 = int(line_cordinates[1])
        x2 = int(line_cordinates[2])
        y2 = int(line_cordinates[3])
        x3 = int(line_cordinates[4])
        y3 = int(line_cordinates[5])
        x4 = int(line_cordinates[6])
        y4 = int(line_cordinates[7])

        if (x2 - x1) != 0:
            k1 = (y2 - y1) / (x2 - x1)
            c1 = y1 - k1 * x1
        else:
            is_parallel_1 = True

        if (x4 - x3) != 0:
            k2 = (y4 - y3) / (x4 - x3)
            c2 = y3 - k2 * x3
        else:
            is_parallel_2 = True

        if is_parallel_1 is False and is_parallel_2 is False:
            if k1 == k2 and c1 == c2:
                print("LINE")
            elif k1 == k2:
                print("NONE")
            else:
                x = (c1 - c2) / (k2 - k1)
                y = k1 * x + c1
                print(f"POINT {string_return(round(x, 2))} {string_return(round(y, 2))}")
        else:
            if is_parallel_1 is True and is_parallel_2 is True:
                if x1 == x3:
                    print("LINE")
                else:
                    print("NONE")

            elif is_parallel_1 is True:
                y = k2 * x1 + c2
                print(f"POINT {string_return(x1)} {string_return(round(y, 2))}")

            else:
                y = k1 * x3 + c1
                print(f"POINT {string_return(x3)} {string_return(round(y, 2))}")

    print("END OF OUTPUT")

def string_return(int_):

    if str(int_).find(".") < 0:
        return str(int_) + ".00"
    elif str(int_).index(".") == len(str(int_)) - 2:
        return str(int_) + "0"
    else:
        return str(int_)


if __name__ == '__main__':
    test_cases = int(input())
    lines_intersecting(test_cases)