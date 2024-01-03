def read_lines(filename):
    with open(filename) as f:
        return f.readlines()


def process_sequence(list_of_numbers):
    if all([x == 0 for x in list_of_numbers]):
        return 0
    diff = []
    previous_element = list_of_numbers[0]
    for i in list_of_numbers[1:]:
        diff.append(i - previous_element)
        previous_element = i
    last_element = process_sequence(diff)
    list_of_numbers.append(last_element + list_of_numbers[-1])
    return list_of_numbers[-1]


def process_sequence_part2(list_of_numbers):
    if all([x == 0 for x in list_of_numbers]):
        return 0
    diff = []
    previous_element = list_of_numbers[0]
    for i in list_of_numbers[1:]:
        diff.append(i - previous_element)
        previous_element = i
    last_element = process_sequence_part2(diff)
    list_of_numbers.insert(0, list_of_numbers[0] - last_element)
    return list_of_numbers[0]


if __name__ == '__main__':
    lines = read_lines('input.txt')
    sum_part_1 = 0
    for line in lines:
        sum_part_1 += process_sequence([int(x) for x in line.split(' ')])
    print("Part 1: ", sum_part_1)
    sum_part_2 = 0
    for line in lines:
        sum_part_2 += process_sequence_part2([int(x) for x in line.split(' ')])
    print("Part 2: ", sum_part_2)
