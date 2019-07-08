from sys import stdin
import math

# phi_1 = (1 + math.sqrt(5)) / 2
# phi_2 = (1 - math.sqrt(5)) / 2
#
fibonnaci_num_cache = {0: 0, 1: 1, 2: 1}


def fibonnaci(n):
    """Cache method -> works only for 1000"""
    if n not in fibonnaci_num_cache.keys():
        fibonnaci_num_cache[n] = fibonnaci(n-1) + fibonnaci(n-2)
    return fibonnaci_num_cache[n]


fibonnaci_nums_cache_2 = {0: 0, 1: 1}


def create_allFibonnaci_nums():
        for i in range(2, 5001):
            fibonnaci_nums_cache_2[i] = fibonnaci_nums_cache_2.get(i - 1) + fibonnaci_nums_cache_2.get(i - 2)


create_allFibonnaci_nums()

for line in stdin:
    """Binet' valem - > works only for 1000"""
    # answer_binat = int((math.pow(phi_1, n) - math.pow(phi_2, n)) / math.sqrt(5))
    n = int(line)

    answer = fibonnaci_nums_cache_2[n]
    print(f"The Fibonacci number for {n} is {answer}")
