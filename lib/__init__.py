#!/usr/bin/env python3

from pathlib import Path

import os

dirname = os.path.dirname(__file__)


def read(day, filename, mapee=None, strip=True):
    path = Path(f"inputs/day{day}/{filename}.txt")

    with open(path) as input_file:
        source = input_file.readlines()
        if strip:
            source = map(str.strip, source)
        if mapee:
            source = map(mapee, source)
        return list(source)
