#!/usr/bin/env python3

import lib
import numpy as np


def one(input_name="one"):
    input_lines = lib.read("07", input_name)
    positions = np.array(input_lines[0].split(","), dtype=int)
    median = int(np.median(positions))
    return np.abs(positions - median).sum()


def fuel(positions, x):
    diff = np.abs(positions - x)
    return ((diff * (diff + 1)) // 2).sum()


def two(input_name="one"):
    input_lines = lib.read("07", input_name)
    positions = np.array(input_lines[0].split(","), dtype=int)
    mean = int(np.mean(positions))
    return min(fuel(positions, x) for x in [mean, mean + 1])
