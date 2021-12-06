#!/usr/bin/env python3

import lib


def balanced(string, scoring):
    brackets = {"(": ")", "[": "]", "<": ">", "{": "}"}
    stack = []
    for c in string:
        if c in brackets.keys():
            stack.append(brackets[c])
        elif c in brackets.values():
            ending = stack.pop()
            if ending != c or ending is None:
                return scoring(c, stack)
    return scoring(0, stack)


def scoring_1(c, stack):
    if c == 0:
        return 0
    return {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }[c]


def scoring_2(c, stack):
    if c != 0:
        return 0
    score = 0
    for c in stack[::-1]:
        score *= 5
        score += {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4,
        }[c]
    return score


def one(input_name="one"):
    input_lines = lib.read("10", input_name)
    return sum([balanced(line, scoring_1) for line in input_lines])


def two(input_name="one"):
    input_lines = lib.read("10", input_name)
    scores = list(
        sorted(filter(int, [balanced(line, scoring_2) for line in input_lines]))
    )
    return scores[len(scores) // 2]
