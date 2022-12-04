from pathlib import Path
from time import perf_counter_ns

from datetime import datetime


def _get_inputs(game_input: str) -> list: return Path(game_input).read_text().splitlines()


def print_solutions(*, game_input: str, part_1: callable = None, part_2: callable = None, descrip: str = "") -> None:
    """"""
    if not any((part_1, part_2)): raise ValueError("At least one function must be provided")
    print((header := f"""{f" SOLUTIONS ":=^35}"""))
    if all((part_1, part_2)):
        for i, solution in enumerate((part_1, part_2), 1):
            message = f"""+ PART {i}: {solution(game_input):.>12,}"""
            print(f"""+ PART {i}: {solution(game_input):.>{12 + len(header) - len(message)},} {descrip}""")
    else:
        i, solution = (1, 2)[part_1 is None], part_1 or part_2
        message = f"""+ PART {i}: {solution(game_input):.>12,}"""
        print(f"""+ PART {i}: {solution(game_input):.>{12 + len(header) - len(message)},} {descrip}""")


def performance_timer(func):
    """"""

    def wrapper(*args, **kwargs):
        begin = f"{datetime.now():%Y-%m-%d %H:%M:%S:%f}"
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        stop = perf_counter_ns()
        print(f"\nSTART: {begin:.>35}")
        print(f"STOP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f'):.>36}")
        print(f"""+ {func.__name__!r} took {(stop - start) / 1_000_000_000:.>20} SECONDS""")
        return result

    return wrapper
