"""04.py
Day 4: Camp Cleanup
https://adventofcode.com/2022/day/4

=============== SOLUTIONS ================
+ PART 1: .............................530
+ PART 2: .............................903
"""
from functools import partial
from itertools import chain, starmap

from utils.helpers import _get_inputs, performance_timer, print_solutions


@performance_timer
def main(game_input: str) -> None:
    part_2 = partial(find_assignment_overlaps, fully_contains=False)
    print_solutions(game_input=game_input, part_1=find_assignment_overlaps, part_2=part_2)


def find_assignment_overlaps(game_input: str, fully_contains: bool = True) -> int:
    """"""
    overlaps = 0
    pairs = chain(*(pair.splitlines() for pair in _get_inputs(game_input)))
    for assignment in pairs:
        check_overlap = (is_intersecting, is_super_or_sub_set)[fully_contains]
        overlap = check_overlap(*(tuple(map(int, elf.split("-"))) for elf in assignment.split(",")))
        if overlap: overlaps += 1
    return overlaps


def is_super_or_sub_set(range1: list, range2: list) -> bool:
    """"""
    start, stop = 0, 1
    r1_range, r2_range = starmap(range, ((range1[start], range1[stop] + 1), (range2[start], range2[stop] + 1)))
    return set(r1_range).issubset(r2_range) or set(r1_range).issuperset(r2_range)


def is_intersecting(range1: list, range2: list) -> bool:
    """"""
    start, stop = 0, -1
    r1_range, r2_range = starmap(range, ((range1[start], range1[stop] + 1), (range2[start], range2[stop] + 1)))
    return bool(list(range(max(r1_range[start], r2_range[start]), min(r1_range[stop], r2_range[stop]) + 1)))


if __name__ == "__main__":
    puzzle_input = r"./data/04_input.txt"
    main(game_input=puzzle_input)
