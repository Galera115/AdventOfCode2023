from dataclasses import dataclass
import re
from math import gcd

@dataclass
class Node:
    name: str
    left: str
    right: str


def read_lines(filename):
    with open(filename) as f:
        return f.readlines()


def parse_node(line):
    name, left, right = re.findall(r'[A-Z]+', line)
    return Node(name, left, right)


def search_node(name, node_list):
    for node in node_list:
        if node.name == name:
            return node


def get_steps(node_list, path, starter_node):
    steps = 0
    found_path = False
    while not found_path:
        for step in path:
            if step == 'L':
                starter_node = search_node(starter_node.left, node_list)
            else:
                starter_node = search_node(starter_node.right, node_list)
            steps += 1
            if starter_node.name == 'ZZZ':
                found_path = True
                break
    return steps

def get_steps_part2(node_list, path, starter_node):
    steps = 0
    found_path = False
    while not found_path:
        for step in path:
            if step == 'L':
                starter_node = search_node(starter_node.left, node_list)
            else:
                starter_node = search_node(starter_node.right, node_list)
            steps += 1
            if starter_node.name[-1] == 'Z':
                found_path = True
                break
    return steps

if __name__ == '__main__':
    lines = read_lines('input.txt')
    path = lines[0].strip()
    nodes = lines[2:]
    node_list = list(map(parse_node, nodes))
    starter_node_part1 = search_node('AAA', node_list)
    steps = get_steps(node_list, path, starter_node_part1)
    print("Part 1: ", steps)
    starter_nodes = list(filter(lambda node: node.name[-1] == 'A', node_list))
    steps_per_node = []
    for starter_node in starter_nodes:
        steps_per_node.append(get_steps_part2(node_list, path, starter_node))
    lcm_part2 = 1
    for i in steps_per_node:
        lcm_part2 = lcm_part2*i//gcd(lcm_part2, i)
    print("Part 2: ", lcm_part2)
