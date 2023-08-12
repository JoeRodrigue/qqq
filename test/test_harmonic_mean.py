import pytest
import sys

from termcolor import colored
from imppkg.harmony import main


@pytest.mark.xfail()
def test_always_fails() -> None:
    raise AssertionError()


def test_always_passes() -> None:
    assert True


@pytest.mark.parametrize(
    "inputs, expected_value",
    [
        ([1, 4, 4], 2.0),
        (["1", "4", "4"], 2.0),
        ([], 0.0),
        (["foo", 4, 4], 0.0),
    ],
)
def test_harmony_happy_path(inputs: list[tuple], expected_value: float, monkeypatch, capsys) -> None:
    # inputs = ['1', '4', '4']
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)

    main()

    # expected_value = 2.0
    assert capsys.readouterr().out.strip() == colored(str(expected_value), "red", "on_white", attrs=["bold"])
