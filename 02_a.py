"""02_a.py
Day 2: Rock Paper Scissors
https://adventofcode.com/2022/day/2

========= SOLUTIONS ==========
+ PART 1: ......15,691 points
+ PART 2: ......12,989 points
"""
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict


def main(game_moves):
    print(f"""{f" SOLUTIONS ":=^30}""")
    print(f"""+ PART 1: {RockPaperScissors().play_1(game_moves).get("you"):.>12,} points""")
    print(f"""+ PART 2: {RockPaperScissors().play_2(game_moves).get("you"):.>12,} points""")


# Define given puzzle vars
_player_grouping = len(player_moves := "A B C X Y Z".split()) >> 1
_points_grouping = len(points := [1, 2, 3, 0, 3, 6]) >> 1
MOVE = "Rock Paper Scissors".split()
OUTCOME = "Lost Draw Won".split()
OPPONENT, YOU = player_moves[:_player_grouping], player_moves[_player_grouping:]
SHAPE_POINTS, OUTCOME_POINTS = points[:_points_grouping], points[_points_grouping:]


@dataclass(match_args=True)
class _GameValues:
    opponent_moves: Dict[str, str] = field(default_factory=lambda: dict(zip(OPPONENT, MOVE)))
    your_moves: Dict[str, str] = field(default_factory=lambda: dict(zip(YOU, MOVE)))
    shape_points: Dict[str, int] = field(default_factory=lambda: dict(zip(MOVE, SHAPE_POINTS)))
    outcome_points: Dict[str, int] = field(default_factory=lambda: dict(zip(OUTCOME, OUTCOME_POINTS)))
    round_end: Dict[str, int] = field(default_factory=lambda: dict(zip(YOU, OUTCOME)))


class RockPaperScissors(_GameValues):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.game_inputs = None
        self.your_score = 0
        self.opponent_score = 0

    def _get_inputs(self, game_inputs: str) -> list:
        return [move.split() for move in Path(game_inputs).read_text().splitlines()]

    def _round_score(self, move, play_1=True) -> dict:
        """Scores of shape selected + outcome"""
        you, opponent = 1, 0
        won, lost, draw = "Won", "Lost", "Draw"
        if play_1:
            pt_shape_opp = self.shape_points[self.opponent_moves[move[opponent]]]
            pt_shape_you = self.shape_points[self.your_moves[move[you]]]
            if pt_shape_you > pt_shape_opp:
                your_round = pt_shape_you + self.outcome_points[won]
                opp_round = pt_shape_opp + self.outcome_points[lost]
            elif pt_shape_you < pt_shape_opp:
                your_round = pt_shape_you + self.outcome_points[lost]
                opp_round = pt_shape_opp + self.outcome_points[won]
            elif pt_shape_you == pt_shape_opp:
                your_round = pt_shape_you + self.outcome_points[draw]
                opp_round = pt_shape_opp + self.outcome_points[draw]
        else:
            predetermined_end = self.round_end.get(move[you])
            pt_shape_opp = self.shape_points[self.opponent_moves[move[opponent]]]
            pt_move_opp = self.opponent_moves[move[opponent]]
            win = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
            lose = {v: k for k, v in win.items()}
            if predetermined_end == won:
                pt_shape_you = self.shape_points[win.get(pt_move_opp)]
                your_round = pt_shape_you + self.outcome_points[won]
                opp_round = pt_shape_opp + self.outcome_points[lost]
            elif predetermined_end == lost:
                pt_shape_you = self.shape_points[lose.get(pt_move_opp)]
                your_round = pt_shape_you + self.outcome_points[lost]
                opp_round = pt_shape_opp + self.outcome_points[won]
                assert pt_shape_you < pt_shape_opp
            elif predetermined_end == draw:
                pt_shape_you = pt_shape_opp
                your_round = pt_shape_you + self.outcome_points[draw]
                opp_round = pt_shape_opp + self.outcome_points[draw]
                assert pt_shape_you == pt_shape_opp
        return {"your_score": your_round, "opponent_score": opp_round}

    def score(self, move, **kwargs) -> tuple:
        round_score = self._round_score(move, **kwargs)
        self.your_score += round_score["your_score"]
        self.opponent_score += round_score["opponent_score"]
        return self.your_score, self.opponent_score

    def play_1(self, game_inputs: str) -> dict:
        moves = self._get_inputs(game_inputs)
        for move in moves: self.score(move)
        return {"you": self.your_score, "opponent": self.opponent_score}

    def play_2(self, game_inputs: str) -> dict:
        moves = self._get_inputs(game_inputs)
        for move in moves: self.score(move, play_1=False)
        return {"you": self.your_score, "opponent": self.opponent_score}


if __name__ == "__main__":
    puzzle_input = r"./data/test.txt"
    main(puzzle_input)
