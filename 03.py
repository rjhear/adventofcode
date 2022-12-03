"""03.py
Day 3
https://adventofcode.com/2022/day/2

============ SOLUTIONS ============
+ PART 1: .......7,917 priority sum
+ PART 2: .......2,585 priority sum
"""
from functools import reduce
from operator import and_
from pathlib import Path
from typing import Generator


def main(game_input: str) -> None:
    print(f"""{f" SOLUTIONS ":=^35}""")
    print(f"""+ PART 1: {run_part_1(game_input):.>12,} priority sum""")
    print(f"""+ PART 2: {run_part_2(game_input):.>12,} priority sum""")


def _get_inputs(game_inputs: str) -> list: return Path(game_inputs).read_text().splitlines()


def find_common_in_rucksack(items: str) -> set:
    """"""
    return set(items[:(compartment := len(items) >> 1)]) & set(items[compartment:])


def find_common_among_rucksacks(rucksacks: list) -> Generator:
    """"""
    return ((reduce(and_, map(set, group))) for group in rucksacks)


def get_priority(dupes: set) -> int:
    """"""
    # {chr(i): ord(chr(i)) for i in range(65, 123) if i not in range(91, 97)}
    return next((ascii_code := ord(dupe)) - 96 + 58 * (1 - ascii_code // 91) for dupe in dupes)


def run_part_1(game_input: str) -> int:
    """"""
    return sum(get_priority(find_common_in_rucksack(items)) for items in _get_inputs(game_input))


def run_part_2(game_input: str, grouping: int = 3) -> int:
    """"""
    rucksacks = _get_inputs(game_input)
    grouped = (rucksacks[n:n + grouping] for n in range(0, len(rucksacks), grouping))
    common = find_common_among_rucksacks(grouped)
    return sum(get_priority(badge) for badge in common)


if __name__ == "__main__":
    puzzle_input = r"./data/03_input.txt"
    main(puzzle_input)
