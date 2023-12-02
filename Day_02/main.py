import regex as re


def read_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines


def split_line(line: str):
    max_num_blues = 0
    max_num_reds = 0
    max_num_greens = 0
    game_id = int(line.split(':')[0].split(' ')[-1])
    game_sets = line.split(':')[1].split(';')
    game_sets = [game_set.split(',') for game_set in game_sets]
    for game_set in game_sets:
        num_blues = 0
        num_reds = 0
        num_greens = 0
        for play in game_set:
            if 'blue' in play:
                num_blues = int(re.findall(r'\d+', play)[0])
            elif 'red' in play:
                num_reds = int(re.findall(r'\d+', play)[0])
            elif 'green' in play:
                num_greens = int(re.findall(r'\d+', play)[0])
        if num_blues > max_num_blues:
            max_num_blues = num_blues
        if num_reds > max_num_reds:
            max_num_reds = num_reds
        if num_greens > max_num_greens:
            max_num_greens = num_greens
    return max_num_blues * max_num_reds * max_num_greens


if __name__ == '__main__':
    lines = read_input('Day_02/input.txt')
    sum = 0
    for line in lines:
        power = split_line(line)
        sum += power
    print(sum)
