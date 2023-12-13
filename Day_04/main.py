def read_input():
    with open('input.txt') as f:
        lines = f.read().split('\n')
    return lines

if __name__ == '__main__':
    lines = read_input()

    # Part 1
    points_part1 = 0

    for line in lines:
        matches = 0
        winning_numbers = line.split(':')[1].split('|')[0].split(' ')
        draw_numbers = line.split(':')[1].split('|')[1].split(' ')

        draw_numbers = [int(x) for x in draw_numbers if x != '']
        winning_numbers = [int(x) for x in winning_numbers if x != '']
        for number in winning_numbers:
            if number in draw_numbers:
                matches += 1
        if matches > 0:
            points_part1 += 2 ** (matches - 1)
    print('Parte 1: {}'.format(points_part1))

    # Part 2
    points_part2 = 0
    num_copies = [1] * len(lines)
    for i, line in enumerate(lines):
        matches = 0
        winning_numbers = line.split(':')[1].split('|')[0].split(' ')
        draw_numbers = line.split(':')[1].split('|')[1].split(' ')

        draw_numbers = [int(x) for x in draw_numbers if x != '']
        winning_numbers = [int(x) for x in winning_numbers if x != '']
        for number in winning_numbers:
            if number in draw_numbers:
                matches += 1
        for j in range(matches):
            num_copies[i+j+1] += 1 * num_copies[i]
    for i in num_copies:
        points_part2 += i
    print('Parte 1: {}'.format(points_part2))
