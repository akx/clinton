from __future__ import annotations

import dataclasses
import os.path
import re
from functools import lru_cache
from re import Pattern


@dataclasses.dataclass
class MapEntry:
    pattern: Pattern
    result: str


@dataclasses.dataclass
class MapResult:
    entry: MapEntry
    match: re.Match

    def __str__(self) -> str:
        return self.entry.result or self.match.group(0)

    def __getitem__(self, key: str) -> str | None:
        try:
            return self.match.group(key)
        except IndexError:
            return None


@dataclasses.dataclass
class MapFile:
    entries: list[MapEntry]

    def find(self, text: str) -> MapResult | None:
        for entry in self.entries:
            if (match := entry.pattern.search(text)) is not None:
                return MapResult(entry=entry, match=match)
        return None

    @classmethod
    def parse_file(cls, filename: str) -> MapFile:
        with open(filename) as f:
            entries = []
            for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                pattern, _, result = (x.strip() for x in line.partition("->"))
                pattern = re.compile(pattern, re.MULTILINE)
                entries.append(MapEntry(pattern=pattern, result=(result or None)))
        return MapFile(entries=entries)


@lru_cache
def get_map(name: str) -> MapFile:
    return MapFile.parse_file(
        os.path.join(os.path.dirname(__file__), "../maps", f"{name}.txt"),
    )
