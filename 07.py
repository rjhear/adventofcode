"""07.py
Day 7: No Space Left On Device
https://adventofcode.com/2022/day/7

=============== SOLUTIONS ================
+ PART 1: .......................1,297,159
+ PART 2: .......................3,866,390
"""
from collections import Counter
from pathlib import Path

from utils.helpers import _get_inputs, performance_timer, print_solutions


@performance_timer
def main(game_input: str) -> None:
    print_solutions(game_input=game_input, part_1=_part_1, part_2=_part_2)


def parse_commands(game_input: str) -> Counter:
    """Given a new line-delimited text file, parse into Counter of paths and sizes.

    @param game_input: str, path to a new line-delimited text file.
    @return: Counter, a dictionary of paths and sizes.
    """
    command_history = _get_inputs(game_input)
    cwd, dirs = Path(), Counter()
    for item in command_history:
        match item.split():
            case ("$", "cd", name):
                cwd = cwd.joinpath(name).resolve()
            case (size, _) if size.isdigit():
                for path in (cwd, *cwd.parents):
                    dirs[path] += int(size)
    return dirs


def _part_1(game_input: str, less_than: int = 100_000) -> int:
    """Given a new line-delimited text file, parse into Counter of paths and sizes.
    Returning the sum of all sizes less than `less_than`

    @param game_input: str, path to a new line-delimited text file.
    @param less_than: int, the maximum size to sum.
    @return: int, the sum of all sizes <= 100,000.
    """
    sizes = parse_commands(game_input).values()
    return sum(size for size in sizes if size <= less_than)


def _part_2(game_input: str) -> int:
    """Given a new line-delimited text file, parse into Counter of paths and sizes.
    Return the minimum size of a file that can be deleted to free up space.

    @param game_input: str, path to a new line-delimited text file.
    @return: int, the minimum size of a file that can be deleted to free up space.
    """
    dirs = parse_commands(game_input)
    sizes = dirs.values()
    disk_space, used_disk_space, unused_disk_space = 70_000_000, dirs[Path("/")], 30_000_000
    available_disk_space = used_disk_space - disk_space + unused_disk_space
    return min(size for size in sizes if size >= available_disk_space)


if __name__ == "__main__":
    puzzle_input: str = r"./data/07_input.txt"
    main(puzzle_input)
