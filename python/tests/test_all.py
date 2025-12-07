import importlib

import pytest

from aoc.tools.files import get_sample_input_file, load_text_file
from aoc.tools.testing import SampleCase, load_test_cases

TESTS = load_test_cases()


@pytest.mark.parametrize("case", TESTS, ids=[c.module_name for c in TESTS])
def test(case: SampleCase):
    data = load_text_file(get_sample_input_file(case.year, case.day))
    mod = importlib.import_module(case.module_name)
    parsed = mod.parse(data)
    assert mod.part1(parsed) == case.ans1
    assert mod.part2(parsed) == case.ans2
