from pathlib import Path


def _get_inputs(game_input: str) -> list: return Path(game_input).read_text().splitlines()


def print_solutions(*, game_input: str, part_1: callable = None, part_2: callable = None, descrip: str = None) -> None:
    """"""
    if not any((part_1, part_2)): raise ValueError("At least one function must be provided")
    print(f"""{f" SOLUTIONS ":=^35}""")
    if all((part_1, part_2)):
        for i, solution in enumerate((part_1, part_2), 1):
            print(f"""+ PART {i}: {solution(game_input):.>12,} {descrip}""")
    else:
        i, solution = (1, 2)[part_2 is None], part_1 or part_2
        print(f"""+ PART {i}: {solution(game_input):.>12,} {descrip}""")
