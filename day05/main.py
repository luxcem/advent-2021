#!/usr/bin/env python3

import lib
import numpy as np


def read_lines(inputs):
    return np.array(
        [line.replace(" -> ", ",").split(",") for line in inputs], dtype=int
    )


def print_diag(lines, grid):
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 != x2 and y1 != y2:
            continue
        x, y = x1, y1
        while x != x2 or y != y2:
            grid[y][x] += 1
            x += np.sign(x2 - x1)
            y += np.sign(y2 - y1)
        grid[y2][x2] += 1


def print_diag_2(lines, grid):
    for line in lines:
        x, y, x2, y2 = line
        while x != x2 or y != y2:
            grid[y][x] += 1
            x += np.sign(x2 - x)
            y += np.sign(y2 - y)
        grid[y2][x2] += 1


def one(input_name="one"):
    input_lines = list(lib.read("05", input_name, str.strip))
    lines = read_lines(input_lines)
    dim = np.max(lines) + 1
    grid = np.zeros((dim, dim))
    print_diag(lines, grid)
    return np.sum(grid >= 2)


def two(input_name="one"):
    input_lines = list(lib.read("05", input_name, str.strip))
    lines = read_lines(input_lines)
    dim = np.max(lines) + 1
    grid = np.zeros((dim, dim))
    print_diag_2(lines, grid)
    return np.sum(grid >= 2)
