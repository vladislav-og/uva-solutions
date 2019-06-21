import sys

line_count = 0
for line in sys.stdin:
    line_count += 1
    if line.strip() == '0' and line_count == 1:
        break

    if line_count == 1:
        try:
            nodes = int(line.strip())
        except:
            line_count -= 1
            continue
        graph_map = [[0 for y in range(nodes)] for x in range(nodes)]
        color_map = [-1] * nodes
    elif line_count == 2:
        edges = int(line.strip())
        if edges == 0:
            line_count = 0
            print("BICOLORABLE.")
            continue

    elif line_count < edges + 2:
        node1 = int(line.strip().split(" ")[0])
        node2 = int(line.strip().split(" ")[1])

        graph_map[node1][node2] = 1
        graph_map[node2][node1] = 1
        # print(graph_map)
    else:
        node1 = int(line.strip().split(" ")[0])
        node2 = int(line.strip().split(" ")[1])

        graph_map[node1][node2] = 1
        graph_map[node2][node1] = 1

        # check if bicolorable
        to_color = [0]
        color_map[0] = 0
        bicolorable = True

        while to_color and bicolorable:
            i = to_color.pop(0)
            print(color_map)
            for node in range(nodes):
                if not graph_map[i][node]:
                    continue
                if color_map[node] == -1:
                    print(i)
                    color_map[node] = color_map[i] + 1
                    to_color.append(node)

                elif color_map[i] == color_map[node]:
                    print(i, " ", node)
                    bicolorable = False
                    break

        if bicolorable:
            print("BICOLORABLE.")
        else:
            print('NOT BICOLORABLE.')

        line_count = 0
