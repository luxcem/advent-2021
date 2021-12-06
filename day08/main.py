#!/usr/bin/env python3

import lib
from collections import Counter


def find_by(patterns, length, intersection=None, intersection_len=None):
    """Find a pattern by looking at number of segment and length of the
    intersection with another number."""
    subset = filter(lambda x: len(x) == length, patterns)
    if intersection:
        subset = filter(lambda x: len(x & intersection) == intersection_len, subset)

    # At this point subset will always contains 1 element
    subset = list(subset)
    assert len(subset) == 1
    patterns.remove(subset[0])
    return subset[0]


def solve(inputs):
    patterns = list(map(set, inputs))
    solution = [set()] * 10
    # Find 1, 4, 7, 8
    solution[1] = find_by(patterns, 2)
    solution[4] = find_by(patterns, 4)
    solution[7] = find_by(patterns, 3)
    solution[8] = find_by(patterns, 7)
    # Find following digits by computing intersection with already found digits
    solution[9] = find_by(patterns, 6, solution[4], 4)
    solution[0] = find_by(patterns, 6, solution[1], 2)
    solution[6] = find_by(patterns, 6, solution[1], 1)
    solution[3] = find_by(patterns, 5, solution[1], 2)
    solution[2] = find_by(patterns, 5, solution[4], 2)
    solution[5] = patterns[0]

    # Frozenset is necessary for a dict key
    solution = list(map(frozenset, solution))
    return {digit_set: i for i, digit_set in enumerate(solution)}


def one(input_name="one"):
    input_lines = lib.read("08", input_name)
    result = 0
    for line in input_lines:
        paterns, digits = map(str.split, line.split("|"))
        solution = solve(paterns.copy())
        counter = Counter([solution[frozenset(digit)] for digit in digits])
        result += counter[1] + counter[4] + counter[7] + counter[8]
    return result


def two(input_name="one"):
    input_lines = lib.read("08", input_name)
    result = 0
    for line in input_lines:
        paterns, digits = map(str.split, line.split("|"))
        solution = solve(paterns.copy())
        result += int(
            "".join(map(str, [solution[frozenset(digit)] for digit in digits]))
        )
    return result
