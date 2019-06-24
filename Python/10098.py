from itertools import permutations, groupby

test_cases = int(input().strip())
for i in range(test_cases):

    perm = permutations(sorted([word for word in input().strip()]))
    for k, v in groupby(sorted(perm)):
        print("".join(k))
    print()

