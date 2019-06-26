from sys import stdin

for line in stdin:
    a, b = int(line.split()[0]), int(line.split()[1])
    print(a * b - 1)
