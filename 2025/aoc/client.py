from __future__ import annotations

import logging
import textwrap
from dataclasses import dataclass
from typing import Literal, Optional

import requests
from bs4 import BeautifulSoup

AOC_BASE_URL = "https://adventofcode.com"


class AoCError(Exception):
    pass


@dataclass
class AoCPuzzle:
    answer_p1: int
    answer_p2: int | None
    text_p1: str
    text_p2: str | None
    sample_input: str


@dataclass
class AoCClient:
    token: str

    @property
    def _session(self) -> requests.Session:
        s = requests.Session()
        s.headers.update(
            {
                "User-Agent": "github.com/yungwood/advent-of-code",
            }
        )
        s.cookies.set("session", self.token, domain=".adventofcode.com")
        return s

    def get_input(self, year: int, day: int) -> str:
        url = f"{AOC_BASE_URL}/{year}/day/{day}/input"
        logging.debug(f"Fetching puzzle input from {url}")
        resp = self._session.get(url)
        if resp.status_code != 200:
            raise AoCError(f"Failed to fetch puzzle input (HTTP {resp.status_code})")
        return resp.text.rstrip("\n")

    def get_puzzle(self, year: int, day: int) -> AoCPuzzle:
        url = f"{AOC_BASE_URL}/{year}/day/{day}"
        logging.debug(f"Fetching puzzle from {url}")
        resp = self._session.get(url)
        if resp.status_code != 200:
            raise AoCError(f"Failed to fetch puzzle input (HTTP {resp.status_code})")
        body = resp.text

        soup = BeautifulSoup(body, "html.parser")
        articles = soup.select("article")
        part1 = articles[0].get_text(strip=True)
        part2 = articles[1].get_text(strip=True) if len(articles) > 1 else None

        example_answers = [
            int(article.select("code em")[-1].get_text()) for article in articles
        ]
        answer1 = example_answers[0]
        answer2 = example_answers[1] if len(example_answers) > 1 else None
        example_input = articles[0].select("pre code")[0].get_text()

        return AoCPuzzle(
            answer_p1=answer1,
            answer_p2=answer2,
            text_p1=part1,
            text_p2=part2,
            sample_input=example_input,
        )
