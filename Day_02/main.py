import regex as re


def read_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines


def split_line(line: str):
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
        if num_blues > 14 or num_greens > 13 or num_reds > 12:
            return 0
    return game_id


if __name__ == '__main__':
    lines = read_input('Day_02/input.txt')
    sum = 0
    for line in lines:
        game_id = split_line(line)
        sum += game_id
    print(sum)
