"""03.py
Day 3
https://adventofcode.com/2022/day/2

============ SOLUTIONS ============
+ PART 1: .......7,917 priority sum
+ PART 2: .......2,585 priority sum
"""
from functools import reduce
from operator import and_
from typing import Generator

from utils.helpers import _get_inputs, print_solutions


def main(game_input: str) -> None:
    print_solutions(game_input=game_input, part_1=run_part_1, part_2=run_part_2)


def find_common_in_rucksack(items: str) -> set:
    """Get the common items in both compartments"""
    return set(items[:(compartment := len(items) >> 1)]) & set(items[compartment:])


def find_common_among_rucksacks(rucksacks: Generator) -> Generator:
    """Get the common items among n rucksacks"""
    return ((reduce(and_, map(set, group))) for group in rucksacks)


def get_priority(dupes: set) -> int:
    """Map the letter to its priority value"""
    # {chr(i): ord(chr(i)) for i in range(65, 123) if i not in range(91, 97)}
    return next((ascii_code := ord(dupe)) - 96 + 58 * (1 - ascii_code // 91) for dupe in dupes)


def run_part_1(game_input: str) -> int:
    """"""
    return sum(map(get_priority, map(find_common_in_rucksack, _get_inputs(game_input))))


def run_part_2(game_input: str, grouping: int = 3) -> int:
    """"""
    rucksacks: list = _get_inputs(game_input)
    grouped = (rucksacks[n:n + grouping] for n in range(0, len(rucksacks), grouping))
    common: Generator = find_common_among_rucksacks(grouped)
    return sum(map(get_priority, common))


if __name__ == "__main__":
    puzzle_input = r"./data/03_input.txt"
    main(puzzle_input)
