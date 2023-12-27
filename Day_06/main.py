import re
from tqdm import tqdm
from functools import reduce


def get_time_and_distances(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    times = [int(s) for s in re.findall(r'\b\d+\b', lines[0])]
    distances = [int(s) for s in re.findall(r'\b\d+\b', lines[1])]
    return times, distances


def parte_uno(times, distances):
    posibles_sol_part_1 = []
    for race_time, race_distance in zip(times, distances):
        pos_sol = 0
        for i in range(race_time):
            dist_recorrida = (race_time - i) * i
            if dist_recorrida > race_distance:
                pos_sol += 1
        posibles_sol_part_1.append(pos_sol)
    return posibles_sol_part_1

if __name__ == '__main__':
    times, distances = get_time_and_distances('input.txt')
    posibles_sol_part_1 = parte_uno(times, distances)
    sol_part1 = reduce(lambda x, y: x * y, posibles_sol_part_1)
    print(f'Parte 1: {sol_part1}')
    times_part2 = [str(t) for t in times]
    times_part2 = reduce(lambda x, y: x + y, times_part2)
    distances_part2 = [str(d) for d in distances]
    distances_part2 = reduce(lambda x, y: x + y, distances_part2)
    times_part2 = [int(s) for s in re.findall(r'\b\d+\b', times_part2)]
    distances_part2 = [int(s) for s in re.findall(r'\b\d+\b', distances_part2)]
    posibles_sol_part2 = parte_uno(times_part2, distances_part2)
    sol_part2 = reduce(lambda x, y: x * y, posibles_sol_part2)
    print(f'Parte 2: {sol_part2}')
