#!/usr/bin/env python3

import lib
import numpy as np


def read_lines(inputs):
    return np.array(
        [line.replace(" -> ", ",").split(",") for line in inputs], dtype=int
    )


def print_diag(lines, grid, only_straight=False):
    for line in lines:
        x, y, x2, y2 = line
        if only_straight and x != x2 and y != y2:
            continue
        while x != x2 or y != y2:
            grid[y][x] += 1
            x += np.sign(x2 - x)
            y += np.sign(y2 - y)
        grid[y2][x2] += 1


def one(input_name="one"):
    input_lines = lib.read("05", input_name)
    lines = read_lines(input_lines)
    dim = np.max(lines) + 1
    grid = np.zeros((dim, dim))
    print_diag(lines, grid, only_straight=True)
    return np.sum(grid >= 2)


def two(input_name="one"):
    input_lines = lib.read("05", input_name)
    lines = read_lines(input_lines)
    dim = np.max(lines) + 1
    grid = np.zeros((dim, dim))
    print_diag(lines, grid)
    return np.sum(grid >= 2)
