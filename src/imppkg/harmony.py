import sys
from termcolor import colored
from imppkg.harmonic_mean import harmonic_mean


def main() -> None:
    result = 0.0
    try:
        nums = _parse_nums(sys.argv[1:])
    except ValueError:
        nums = [result]
    try:
        result = _calculate_results(nums)
    except ZeroDivisionError:
        pass
    print(_format_output(result))


def _parse_nums(nums: list[str]) -> list[float]:
    return [float(n) for n in nums]


def _calculate_results(nums: list[float]) -> float:
    return harmonic_mean(nums)


def _format_output(result: float) -> str:
    return colored(str(result), "red", "on_white", attrs=["bold"])
