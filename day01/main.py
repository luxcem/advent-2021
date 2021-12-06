#!/usr/bin/env python3

import lib


def one(input_name="one"):
    input_lines = lib.read("01", input_name)
    lines = map(int, map(str.strip, input_lines))
    previous = None
    diff = [0] * len(input_lines)
    for i, line in enumerate(lines):
        if previous and line > previous:
            diff[i] = 1
        elif previous and line < previous:
            diff[i] = -1
        previous = line
    return diff.count(1)


def two(input_name="one"):
    input_lines = lib.read("01", input_name)
    lines = list(map(int, map(str.strip, input_lines)))
    n = len(lines)
    count = 0
    for i in range(1, n - 1):
        a = sum(lines[i - 1 : i + 2])
        b = sum(lines[i : i + 3])
        if b > a:
            count += 1
    return count
