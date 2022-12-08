"""06.py
Day 6: Tuning Trouble
https://adventofcode.com/2022/day/6

=============== SOLUTIONS ================
+ PART 1: ...........................1,804
+ PART 2: ...........................2,508
"""
from functools import partial

from utils.helpers import _get_inputs, performance_timer, print_solutions


@performance_timer
def main(game_input: str) -> None:
    find_signal_14 = partial(find_signal, base_len=14)
    print_solutions(game_input=game_input, part_1=find_signal, part_2=find_signal_14)


def find_signal(game_input: str, base_len: int = 4) -> int:
    packets: str = _get_inputs(game_input)[0]
    collector = ""
    if len(set(packets[:(base_len)])) == base_len:
        return base_len
    collector += packets[:base_len]
    for idx, marker in enumerate(packets):
        collector += packets[base_len + idx]
        if is_all_unique(collector[-base_len:]):
            return len(collector)
    return 0


def is_all_unique(x: str) -> bool: return len(set(x)) == len(x)


if __name__ == "__main__":
    puzzle_input = r"./data/06_input.txt"
    main(puzzle_input)
