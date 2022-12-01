import sys

import requests


class Calorimeter:
    @staticmethod
    def max(inventories: [[int]]):
        return max([sum(inventory) for inventory in inventories])

    @staticmethod
    def top3(inventories: [[int]]):
        aggregated = [sum(inventory) for inventory in inventories]
        return sum(sorted(aggregated)[-3:])


class Parser:
    @staticmethod
    def parse(lines: [str]):
        output = []
        inventory = []
        for line in lines:
            if len(line) == 0:
                output += inventory,
                inventory = []
            else:
                inventory += int(line),
        output += inventory,
        return output


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        parsed = Parser.parse([line.strip() for line in file.readlines()])
        print("TOP 1:")
        print(Calorimeter.max(parsed))

        print("TOP 3:")
        print(Calorimeter.top3(parsed))
