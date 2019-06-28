from sys import stdin


def random_num_count(num):

    count = 0
    memory = {}
    while True:
        memory[int(num)] = 1

        count += 1
        num *= num
        num = num / 100
        num = int(num % 10000)

        if num in memory.keys():
            break

    print(count)


for num in stdin:
    if num.strip() == "0":
        break

    random_num_count(int(num.strip()))

