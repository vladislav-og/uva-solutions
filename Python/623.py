from sys import stdin

for line in stdin:
    n = int(line)
    answer = 1
    for i in range(2, n + 1):
        answer *= i
    print(line.strip() + "!")
    print(answer)
