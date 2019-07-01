

def overlaping(test_cases):
    for i in range(test_cases):
        if i != 0:
            print()

        input_ = input()
        while input_ == '':
            input_ = input()

        rect_1 = input_.strip().split(" ")
        rect_2 = input().strip().split(" ")

        x1_ll = int(rect_1[0])
        y1_ll = int(rect_1[1])
        x1_ur = int(rect_1[2])
        y1_ur = int(rect_1[3])

        x2_ll = int(rect_2[0])
        y2_ll = int(rect_2[1])
        x2_ur = int(rect_2[2])
        y2_ur = int(rect_2[3])

        X1 = max(x1_ll, x2_ll)
        X2 = min(x1_ur, x2_ur)

        # print(X1 + ' ' + X2)
        # print(x1_ll, y1_ll, x1_ur, y1_ur, x2_ll, y2_ll, x2_ur, y2_ur)
        if X1 >= X2:
            print("No Overlap")
            continue

        Y1 = max(y1_ll, y2_ll)
        Y2 = min(y1_ur, y2_ur)

        if Y1 >= Y2:
            print("No Overlap")
            continue

        print(f'{X1} {Y1} {X2} {Y2}')




if __name__ == '__main__':
    test_cases = int(input())
    overlaping(test_cases)
