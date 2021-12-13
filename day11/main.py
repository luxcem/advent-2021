#!/usr/bin/env python3

import lib
import numpy as np

directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]


def inc_adj(grid, i, j, lighted):
    for (ydiff, xdiff) in directions:
        y, x = i + ydiff, j + xdiff
        if y >= 0 and y < grid.shape[0] and x >= 0 and x < grid.shape[1]:
            if (y, x) not in lighted:
                grid[i + ydiff][j + xdiff] += 1


def step_light(grid, lighted):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] > 9 and (i, j) not in lighted:
                lighted.append((i, j))
                grid[i][j] = 0
                inc_adj(grid, i, j, lighted)
    return lighted


def step(grid):
    grid += 1
    lighted = []
    keep_going = True
    while keep_going:
        prev_len = len(lighted)
        new_lighted = step_light(grid, lighted)
        if len(new_lighted) == prev_len:
            keep_going = False
        lighted = new_lighted
    return len(lighted)


def one(input_name="one"):
    input_lines = lib.read("11", input_name)
    grid = np.array([[c for c in line] for line in input_lines], dtype=int)
    n_step = 100
    n_lighted = 0
    for i in range(n_step):
        n_lighted += step(grid)
    return n_lighted


def two(input_name="one"):
    input_lines = lib.read("11", input_name)
    grid = np.array([[c for c in line] for line in input_lines], dtype=int)
    grid_size = grid.shape[0] * grid.shape[1]
    n_step = 0
    while True:
        n_lighted = step(grid)
        n_step += 1
        if n_lighted == grid_size:
            return n_step
