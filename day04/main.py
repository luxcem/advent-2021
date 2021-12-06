#!/usr/bin/env python3

import lib
import numpy as np


def read_grids(inputs):
    grids = []
    current_grid = []
    for line in inputs:
        if line == "":
            grids.append(current_grid)
            current_grid = []
        else:
            current_grid.append(list(map(int, line.split())))

    grids.append(current_grid)
    return np.array(grids)


def check_victory(grids, cache):
    for n in range(len(grids)):
        if np.any(np.all(cache[n], axis=1)):
            return n
        if np.any(np.all(cache[n], axis=0)):
            return n
    return False


def check_victory_2(grid, cache):
    if np.any(np.all(cache, axis=1)):
        return True
    if np.any(np.all(cache, axis=0)):
        return True
    return False


def score(grid, cache, number):
    return np.sum(grid[cache == 0]) * number


def one(input_name="one"):
    input_lines = lib.read("04", input_name)
    numbers = map(int, input_lines[0].split(","))
    grids = read_grids(input_lines[2:])
    cache = np.zeros(grids.shape)
    for number in numbers:
        cache[grids == number] = 1
        check = check_victory(grids, cache)
        if check is not False:
            return score(grids[check], cache[check], number)


def two(input_name="one"):
    input_lines = lib.read("04", input_name)
    numbers = map(int, input_lines[0].split(","))
    grids = read_grids(input_lines[2:])
    n = grids.shape[0]
    cache = np.zeros(grids.shape)
    wons = []
    scores = []
    for number in numbers:
        cache[grids == number] = 1
        for i in range(n):
            if i in wons:
                continue
            if check_victory_2(grids[i], cache[i]):
                current_score = score(grids[i], cache[i], number)
                scores.append((i, current_score))
                wons.append(i)
    return scores[-1][1]
