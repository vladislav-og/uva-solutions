import sys

total_input = []
output_list = []
output_dict = {}

for line in sys.stdin:

    if line.strip() == '#':
        break

    input_line = line.strip().split(' ')
    total_input += input_line


sorted_word_list = ["".join(sorted(word.lower())) for word in total_input]

for i, word in enumerate(sorted_word_list):
    if word in output_dict.keys():
        output_dict[word] = output_dict[word] + [total_input[i]]
    else:
        output_dict[word] = [total_input[i]]

for value in output_dict.values():
    if len(value) == 1:
        output_list.append(value[0])

for word in sorted(output_list):
    print(word)