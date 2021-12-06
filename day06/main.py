#!/usr/bin/env python3

import lib
from collections import Counter
import numpy as np


def one_day(fishes):
    new_born = fishes[0]
    for i in range(8):
        fishes[i] = fishes[i + 1]
    fishes[6] += new_born
    fishes[8] = new_born


def one_slow(input_name="one", n=80):
    input_lines = list(lib.read("06", input_name, str.strip))
    fishes = map(int, input_lines[0].split(","))
    cache = Counter(fishes)
    for i in range(n):
        one_day(cache)
    return sum(cache.values())


def two_slow(input_name="one"):
    return one_slow(input_name, 256)


def one(input_name="one", n=80):
    input_lines = list(lib.read("06", input_name, str.strip))
    fishes = map(int, input_lines[0].split(","))
    cache = Counter(fishes)
    init = np.array([cache[i] for i in range(9)], dtype="object")
    A = np.array(
        [
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
        dtype="object",
    )
    B = np.linalg.matrix_power(A, int(n))
    return B.dot(init).sum()


def two(input_name="one"):
    return one(input_name, 256)
