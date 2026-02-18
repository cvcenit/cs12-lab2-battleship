# pyright: strict

from collections.abc import Sequence
from random import Random
from string import ascii_uppercase


def generate_grid(n: int, ship_sizes: Sequence[int], rng: Random) -> list[list[str]]:
    grid = [["."] * n for _ in range(n)]

    for ship_index, ship_size in enumerate(ship_sizes):
        orie = rng.choice("VH")

        def poss_gen():
            def good(i: int, j: int, k: int) -> bool:
                _i = i + (k if orie == "V" else 0)
                _j = j + (k if orie == "H" else 0)
                return 0 <= _i < n and 0 <= _j < n and grid[_i][_j] == "."

            for i in range(n):
                for j in range(n):
                    if all(good(i, j, k) for k in range(ship_size)):
                        yield (i, j)

        poss = [*poss_gen()]
        i, j = rng.choice(poss)

        for k in range(ship_size):
            _i = i + (k if orie == "V" else 0)
            _j = j + (k if orie == "H" else 0)
            grid[_i][_j] = ascii_uppercase[ship_index]

    return grid