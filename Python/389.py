import sys

convert = "0123456789ABCDEF"


def int2base(value: int, base: int):
    builder = ""
    while value > 0:
        rem = int(value % base)
        value = (value - rem) / base
        builder += convert[rem]
    return builder[::-1]


def toDec(value, base:int):
    sum = 0
    for i, x in enumerate(value[::-1]):
        sum += convert.index(x) * base**i
    return sum


if "main" == name:

    for line in sys.stdin:
        data = str(line).strip()
        data = data.split()

        if data[0].isnumeric() and int(data[0]) == 0:
            print("      0")
            continue
        answer = int2base(toDec(data[0], int(data[1])), int(data[2]))
        if len(answer) < 8:
            print('{:>7}'.format(answer))
        else:
            print("  ERROR")