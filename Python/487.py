

def init_map():
    input()
    map_size = int(input())

    game_map = []
    for i in range(map_size):
        game_map.append(list(input()))
    return game_map


def find_words(game_map):
    map_size = len(game_map)
    output = []

    for i in range(map_size):
        for j in range(map_size):
            output += check_neighbours(i, j, game_map, [], game_map[i][j])

    filtered_output = set(output)

    sorted_output = sorted(filtered_output, key=lambda x: (len(x), x))
    if filtered_output is not None:
        for i in sorted_output:
            print(i)


def check_neighbours(i, j, game_map, output, string):
    map_size = len(game_map)

    neighbors = [(0 if i - 1 <= 0 else i - 1, 0 if j - 1 <= 0 else j - 1),
                 (0 if i - 1 <= 0 else i - 1, j),
                 (0 if i - 1 <= 0 else i - 1, j + 1 if j + 1 <= map_size - 1 else j),

                 (i, 0 if j - 1 <= 0 else j - 1),
                 (i, j + 1 if j + 1 <= map_size - 1 else j),

                 (i + 1 if i + 1 <= map_size - 1 else i, 0 if j - 1 <= 0 else j - 1),
                 (i + 1 if i + 1 <= map_size - 1 else i, j),
                 (i + 1 if i + 1 <= map_size - 1 else i, j + 1 if j + 1 <= map_size - 1 else j),
                 ]

    neighbors = set(neighbors)
    neighbors.discard((i, j))
    for n in neighbors:
        if ord(game_map[i][j]) < ord(game_map[n[0]][n[1]]):
            check_neighbours(n[0], n[1], game_map, output, string + game_map[n[0]][n[1]])
        if len(string) >= 3:
            output.append(string)

    return output


if __name__ == '__main__':
    testcases = input()

    for i in range(int(testcases)):
        find_words(init_map())
        if i < int(testcases) - 1:
            print()

