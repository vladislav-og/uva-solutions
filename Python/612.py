datasets = int(input())


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    result = 0
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
                result += 1
        passnum = passnum - 1
    return result


for x in range(datasets):
    input()
    if x != 0:
        print()
    data = input().split(" ")
    listike = []
    result = {}
    for y in range(int(data[1])):
        line = input()
        listike.append(line)
        result[line] = shortBubbleSort(list(line))
    print("\n".join(sorted(listike, key=lambda x: result[x])))
