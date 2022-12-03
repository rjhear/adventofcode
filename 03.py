"""03.py
Day 3
https://adventofcode.com/2022/day/2

============ SOLUTIONS ============
+ PART 1: .......7,917 priority sum

"""
from pathlib import Path


def main(game_input) -> None:
    print(f"""{f" SOLUTIONS ":=^35}""")
    print(f"""+ PART 1: {run_part_1(game_input):.>12,} priority sum""")

    
def _get_inputs(game_inputs):
    return Path(game_inputs).read_text().splitlines()


def get_intersection(string: str) -> set:
    """"""
    return set(string[:(split := len(string) >> 1)]) & set(string[split:])


def get_priority(dupes: set) -> int:
    """"""
    # print({chr(i): ord(chr(i)) for i in range(65, 123) if i not in range(91, 97)})
    return next((ascii_code := ord(dupe)) - 96 + 58 * (1 - ascii_code // 91) for dupe in dupes)


def run_part_1(game_input: str) -> int:
    return sum(get_priority(get_intersection(items)) for items in _get_inputs(game_input))


def run_part_2():
    ...


if __name__ == "__main__":
    puzzle_input = r"./data/03_input.txt"
    main(puzzle_input)
