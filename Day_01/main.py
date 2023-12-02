import regex as re


def read_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines


def get_numbers(line):
    digits_letters = ['one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight', 'nine']
    all_numbers = re.findall(r'\d|' + r'|'.join(digits_letters), line, overlapped=True)
    for number in all_numbers:
        if number in digits_letters:
            all_numbers[all_numbers.index(number)] = digits_letters.index(number) + 1
        else:
            all_numbers[all_numbers.index(number)] = int(number)
    return all_numbers


if __name__ == '__main__':
    lines = read_input('Day_01/input.txt')
    sum = 0
    for line in lines:
        numbers = get_numbers(line)
        sum += numbers[0]*10 + numbers[-1]
    print(sum)
