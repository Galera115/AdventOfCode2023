from re import findall


def read_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    lines = read_input('Day_01/input.txt')
    sum = 0
    for line in lines:
        numbers = [int(x) for x in line if x.isdigit()]
        sum += numbers[0]*10 + numbers[-1]
    print(sum)