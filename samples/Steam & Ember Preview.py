"""A compact syntax sample for the Steam & Ember color schemes."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Final


DEFAULT_TEMPERATURE: Final[int] = 67


class Roast(str, Enum):
    LIGHT = "light"
    MEDIUM = "medium"
    DARK = "dark"


@dataclass(frozen=True, slots=True)
class Coffee:
    name: str
    roast: Roast = Roast.MEDIUM
    temperature: int = DEFAULT_TEMPERATURE

    @property
    def label(self) -> str:
        return f"{self.name} · {self.roast.value} · {self.temperature}°C"

    def serve(self, *, with_sugar: bool = False) -> dict[str, str | bool]:
        """Return a small order payload."""
        return {
            "label": self.label,
            "with_sugar": with_sugar,
            "note": "slow down and make it well",
        }


def load_menu(path: Path | None = None) -> list[Coffee]:
    # Comments should be visible without competing with the code.
    source = path or Path("menu.txt")
    if not source.exists():
        return [Coffee("Flat White"), Coffee("Espresso", Roast.DARK, 63)]

    return [
        Coffee(name.strip())
        for name in source.read_text(encoding="utf-8").splitlines()
        if name.strip()
    ]


if __name__ == "__main__":
    for cup in load_menu():
        print(cup.serve(with_sugar=False))
