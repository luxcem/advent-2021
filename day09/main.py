#!/usr/bin/env python3

import lib
import numpy as np
import scipy.signal


def min_coords(floor_map):
    h, w = floor_map.shape
    floor_map = np.pad(floor_map, pad_width=1, mode="constant", constant_values=9)
    min_0 = set(zip(*scipy.signal.argrelmin(floor_map, axis=0)))
    min_1 = set(zip(*scipy.signal.argrelmin(floor_map, axis=1)))
    return np.array(list(min_0 & min_1)) - 1


def one(input_name="one"):
    input_lines = lib.read("09", input_name)
    floor_map = np.array([[int(d) for d in line] for line in input_lines])
    coords = min_coords(floor_map)
    return (floor_map[coords[:, 0], coords[:, 1]] + 1).sum()


def flood_fill_min(floor_map, y, x, visited=None):
    total = 1
    if visited is None:
        visited = []
    visited.append((y, x))
    total = 1
    for (i, j) in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
        outside = i < 0 or i >= floor_map.shape[0] or j < 0 or j >= floor_map.shape[1]
        if outside or (i, j) in visited:
            continue
        if floor_map[i][j] > floor_map[y][x] and floor_map[i][j] != 9:
            total += flood_fill_min(floor_map, i, j, visited)
    return total


def two(input_name="one"):
    input_lines = lib.read("09", input_name)
    floor_map = np.array([[int(d) for d in line] for line in input_lines])
    coords = min_coords(floor_map)
    bassins = [flood_fill_min(floor_map, i, j) for (i, j) in coords]
    return np.prod(sorted(bassins)[-3:])
