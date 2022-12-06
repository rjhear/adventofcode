"""05.py
Day 5: Supply Stacks
https://adventofcode.com/2022/day/5

=============== SOLUTIONS ================
+ PART 1: .......................ZSQVCCJLL
+ PART 2: .......................QZFJRWHGS
"""
from collections import deque

from utils.helpers import _get_inputs, performance_timer, print_solutions


@performance_timer
def main(game_input: str) -> None:
    print_solutions(game_input=game_input, part_1=run_part_1, part_2=run_part_2)


def run_part_1(game_input: str) -> str:
    """"""
    stacks, moves, gameboard = _process_input(game_input)
    for move in moves:
        quantity, beg, end = tuple(move)
        for _ in range(quantity):
            gameboard.get(end).append(gameboard.get(beg).pop())
    return "".join(stack.pop() for stack in gameboard.values())


def run_part_2(game_input: str) -> str:
    """"""
    stacks, moves, gameboard = _process_input(game_input)
    for move in moves:
        quantity, beg, end = tuple(move)
        crane = [gameboard.get(beg).pop() for _ in range(quantity)]
        while crane:
            gameboard.get(end).append(crane.pop())
    return "".join(stack.pop() for stack in gameboard.values())


def _process_input(game_input: str) -> tuple:
    """"""
    info = _get_inputs(game_input)
    stacks, moves = info[:(cut_off := info.index(""))], info[cut_off + 1:]
    stacks.pop(-1)
    stacks = [j[::-1] for parts in zip(*stacks) if (j := [part for part in parts if part.isalpha()])]
    moves = ((int(i) for i in move.split() if i.isdigit()) for move in list(moves))
    gameboard = dict(enumerate(map(deque, stacks), 1))
    return stacks, moves, gameboard


if __name__ == "__main__":
    puzzle_input = r"./data/05_input.txt"
    main(puzzle_input)
