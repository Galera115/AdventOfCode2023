from dataclasses import dataclass
import re

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

if __name__ == '__main__':
    lines = read_lines('input.txt')
    path = lines[0].strip()
    nodes = lines[2:]
    node_list = list(map(parse_node, nodes))
    steps = 0
    actual_node = search_node('AAA', node_list)
    found_path = False
    while not found_path:
        for step in path:
            if step == 'L':
                actual_node = search_node(actual_node.left, node_list)
            else:
                actual_node = search_node(actual_node.right, node_list)
            steps += 1
            if actual_node.name == 'ZZZ':
                found_path = True
                break
    print(steps)
