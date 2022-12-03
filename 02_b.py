"""02.py
Day 2: Rock Paper Scissors
https://adventofcode.com/2022/day/2

========= SOLUTIONS ==========
+ PART 1: ......15,691 points
+ PART 2: ......12,989 points
"""
from pathlib import Path

PLAYER_MOVES = "A B C X Y Z"
WIN = {"A": "Paper", "B": "Scissors", "C": "Rock"}
LOSE_1 = {"X": "Scissors", "Y": "Rock", "Z": "Paper"}
LOSE_2 = {"A": "Scissors", "B": "Rock", "C": "Paper"}


def main(game_moves):
    rounds = _get_inputs(game_moves)
    print(f"""{f" SOLUTIONS ":=^30}""")
    print(f"""+ PART 1: {run_part_1(rounds):.>12,} points""")
    print(f"""+ PART 2: {run_part_2(rounds):.>12,} points""")


def _get_inputs(game_inputs: str) -> list:
    return [tuple(move.split()) for move in Path(game_inputs).read_text().splitlines()]


def lookup_game_vals(term):
    game_vals = {("Rock", "A", "X", 1): 1, ("Paper", "B", "Y", 2): 2, ("Scissors", "C", "Z", 3): 3}
    for lookup in game_vals:
        if term in lookup:
            return game_vals.get(lookup)


def get_outcome_val(opp_shape, you_shape):
    rules = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
    if you_shape == opp_shape:
        return 3
    elif rules.get(you_shape) == opp_shape:
        return 0
    else:
        return 6


def run_part_1(rounds):
    opponent, you = 0, 1
    your_total_score_1 = 0
    for round in rounds:
        you_score = lookup_game_vals(round[you])
        outcome_pts = get_outcome_val(WIN.get(round[opponent]), LOSE_1.get(round[you]))
        your_total_score_1 += (you_score + outcome_pts)
    return your_total_score_1


def run_part_2(rounds):
    opponent, ending = 0, 1
    your_total_score_2 = 0
    for round in rounds:
        if round[ending] in ("Y", "Draw"):
            you_score, outcome_pts = lookup_game_vals(round[opponent]), 3
        elif round[ending] in ("X", "Lose"):
            you_score = lookup_game_vals(LOSE_2.get(round[opponent]))
            outcome_pts = get_outcome_val(LOSE_2.get(round[opponent]), WIN.get(round[opponent]))
        elif round[ending] in ("Z", "Win"):
            you_score = lookup_game_vals(WIN.get(round[opponent]))
            outcome_pts = get_outcome_val(WIN.get(round[opponent]), LOSE_2.get(round[opponent]))
        your_total_score_2 += (you_score + outcome_pts)
    return your_total_score_2


if __name__ == "__main__":
    puzzle_input = r"./data/02_input.txt"
    main(puzzle_input)

"""
import numpy as np
int totalScore = Arrays.stream(contents.split("\n")) 
   .map(String::toCharArray) 
   .map(chars -> new int[]{chars[0] - 64, chars[2] - 87}) 
   .mapToInt(shapes -> ((int) Math.sin((int) ((shapes[1] - shapes[0]) * 1.5) * Math.PI / 2) * 3 + 3) + shapes[1]) 
   .sum()
# charcters = [65, 66, 67, 88, 89, 90]
    # rps_vals = {65: 1, 66: 2, 67: 3, 88: 1, 89: 2, 90: 3}
    # moves = [tuple(rps_vals.get(ord(char)) for char in move) for move in _get_inputs(game_moves)]
"""
