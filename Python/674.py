import sys

coins = [50, 25, 10, 5, 1]
cache = {}


def dif_ways(index, amount):

    if index >= 5:
        if amount == 0:
            return 1
        else:
            return 0

    if (index, amount) in cache.keys():
        return cache[index, amount]
    value1, value2 = 0, 0
    if index <= len(coins) - 1:
        if amount - coins[index] >= 0:
            value1 = dif_ways(index, amount - coins[index])

    value2 = dif_ways(index + 1, amount)
    cache[(index, amount)] = value1 + value2
    return cache[(index, amount)]


for line in sys.stdin:
        amount = int(line.strip())
        print(dif_ways(0, amount))



