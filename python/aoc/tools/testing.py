from dataclasses import dataclass

from aoc.tools.files import get_tests_file, load_text_file


@dataclass(frozen=True)
class SampleCase:
    year: int
    day: int
    ans1: int
    ans2: int

    @property
    def module_name(self):
        return f"{self.year}.day{self.day:02d}"


def load_test_cases() -> list[SampleCase]:
    cases: list[SampleCase] = []

    for raw in get_tests_file().read_text().splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue

        year, day, ans1, ans2 = map(int, line.split())
        cases.append(SampleCase(year, day, ans1, ans2))

    return cases


def write_test_cases(cases: list[SampleCase]) -> None:
    cases.sort(key=lambda c: (c.year, c.day))
    lines = ["# year day ans1 ans2"]
    for case in cases:
        lines.append(f"{case.year} {case.day} {case.ans1} {case.ans2}")
    text = "\n".join(lines)
    get_tests_file().write_text(text)


def upsert_test_case(case: SampleCase) -> None:
    tests = load_test_cases()
    for test in tests:
        if test.year == case.year and test.day == case.day:
            tests.remove(test)
            break
    tests.append(case)
    write_test_cases(tests)
