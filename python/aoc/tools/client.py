from __future__ import annotations

import logging
import os
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

from aoc.tools.files import get_cache_folder, load_text_file
from aoc.tools.formatting import render

AOC_BASE_URL = "https://adventofcode.com"


class AoCError(Exception):
    pass


@dataclass
class AoCPuzzle:
    answers: list[int]
    texts: list[str]
    sample_input: str


@dataclass
class AoCClient:

    @property
    def _session(self) -> requests.Session:
        token = os.getenv("AOC_SESSION")
        if token is None:
            raise AoCError("AOC_SESSION is not set!")
        s = requests.Session()
        s.headers.update(
            {
                "User-Agent": "github.com/yungwood/advent-of-code",
            }
        )
        s.cookies.set("session", token, domain=".adventofcode.com")
        return s

    def get(self, path: str, ignore_cache: bool = False) -> str:
        filename = path.replace("/", "_")
        cache_file = get_cache_folder() / f"{filename}.html"
        if cache_file.exists() and not ignore_cache:
            logging.debug(f"Reading cached result from {cache_file}")
            return load_text_file(cache_file)
        else:
            url = f"{AOC_BASE_URL}/{path}"
            logging.debug(f"Fetching {url}")
            resp = self._session.get(url)
            if resp.status_code != 200:
                raise AoCError(
                    f"Failed to fetch puzzle input (HTTP {resp.status_code})"
                )
            body = resp.text
            logging.debug(f"Caching result to {cache_file}")
            cache_file.write_text(body)
        return body

    def get_input(self, year: int, day: int) -> str:
        url = f"{year}/day/{day}/input"
        return self.get(url).rstrip("\n")

    def get_puzzle(self, year: int, day: int, ignore_cache: bool = False) -> AoCPuzzle:
        body = self.get(f"{year}/day/{day}", ignore_cache)

        soup = BeautifulSoup(body, "html.parser")
        articles = soup.select("article")
        texts = []
        answers = []
        for article in articles:
            texts.append(render(article))
            values = article.select("code em")
            if not values:
                values = article.select("em code")
            answers.append(int(values[-1].get_text()) if values else 0)
        example_input = articles[0].select("pre code")[0].get_text()

        return AoCPuzzle(
            answers=answers,
            texts=texts,
            sample_input=example_input,
        )
