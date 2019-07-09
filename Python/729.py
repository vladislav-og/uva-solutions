from itertools import product

datasets = int(input())

for x in range(datasets):
    input()
    if x != 0:
        print()

    data = input().split(" ")
    n = int(data[0])
    h = int(data[1])

    answer = []

    for i in ["".join(seq) for seq in product("01", repeat=n)]:
        count = 0
        for chr in i:
            if chr == "1":
                count += 1
        if count == h:
            answer.append(i)

    print("\n".join(answer))
