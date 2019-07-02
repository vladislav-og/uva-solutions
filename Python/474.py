import sys


def func_474(number, values, powers):
    answer = 1
    power = 0
    if number in values:
        answer = values[number]
        power = powers[number]
    else:
        for i in range(number + 1):
            if i in values and i in powers:
                answer = values[i]
                power = powers[i]
            elif i > 0:
                answer = answer / 2
                if answer < 1:
                    answer = answer * 10
                    power -= 1
                values[i] = answer
                powers[i] = power
    rounded_answer = str(round(answer, 3))
    if len(rounded_answer) == 1:
        rounded_answer += "."
    while len(rounded_answer) < 5:
        rounded_answer += "0"
    print("2^-" + str(number) + " = " + rounded_answer + "e" + str(power))


if __name__ == '__main__':
    values_dict = {0: 1}
    powers_dict = {0: 0}
    for line in sys.stdin:
        func_474(int(line), values_dict, powers_dict)
