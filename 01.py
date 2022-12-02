"""01.py
Day 1: Calorie Counting
https://adventofcode.com/2022/day/1

========= SOLUTIONS ==========
+ PART 1 ......65,912 calories
+ PART 2 .....195,625 calories
"""
from itertools import groupby
from pathlib import Path


def main(calories: str = None) -> None:
    print(f"""{f" SOLUTIONS ":=^30}""")
    print(f"""+ PART 1 {get_max_cals(elf_cals := get_elf_cal_totals(calories)):.>12,} calories""")
    print(f"""+ PART 2 {sum_top_n_max_cals(elf_cals):.>12,} calories""")


def get_elf_cal_totals(filepath: str) -> dict:
    """Read in, split into groups, and return sequential mapping of k-elf, v-total_calories"""
    calorie_groups = (sum(map(int, cals))
                      for elf, cals in groupby(Path(filepath).read_text().splitlines(), bool)
                      if elf)
    return dict(enumerate(calorie_groups, start=1))


def get_max_cals(elf_calories: dict) -> int | str:
    """Part 1: Find max cals and check dupes"""
    most: int = max(all_cals := list(elf_calories.values()))
    isDupe: bool = (dupe_count := all_cals.count(most)) > 1
    return (most, f"{dupe_count} elves have {most:,} calories")[isDupe]


def sum_top_n_max_cals(elf_calories: dict, n: int = 3) -> int:
    """Part 2: Get top n and sum"""
    return sum(sorted(elf_calories.values())[-n:])


if __name__ == "__main__":
    puzzle_input = r"./data/01_input.txt"
    main(puzzle_input)

# os.linesep
