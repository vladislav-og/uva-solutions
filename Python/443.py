import sys
import itertools
import heapq


def humble_numbers_gen():
    primes = (2, 3, 5, 7)
    result = [1]

    primes_list = map(lambda x: (x * result[i] for i in range(6000)), primes)

    merged = heapq.merge(*primes_list)
    for k, _ in itertools.groupby(merged):
        result.append(k)

    return result


humble_list = humble_numbers_gen()

for number in sys.stdin:
    if number.strip() == "0":
        break

    number = number.strip()
    if list(number)[-1] == '1':
        print(f"The {number}st humble number is {humble_list[int(number) - 1]}.")
    elif list(number)[-1] == '2':
        print(f"The {number}nd humble number is {humble_list[int(number) - 1]}.")
    elif list(number)[-1] == '3':
        print(f"The {number}rd humble number is {humble_list[int(number) - 1]}.")
    else:
        print(f"The {number}th humble number is {humble_list[int(number) - 1]}.")
