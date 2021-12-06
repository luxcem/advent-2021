#!/usr/bin/env python3

import lib
import numpy as np


def bin_array_to_int(value):
    return int("".join(value.astype(int).astype(str)), 2)


def common(matrix):
    value = np.mean(matrix, axis=0)
    value = np.heaviside(value - 0.5, 1).astype(int)
    opposite = abs(value - 1)
    return (value, opposite)


def read_matrix(input_lines):
    n = len(input_lines)
    m = len(input_lines[0])

    matrix = np.zeros((n, m))
    for i, line in enumerate(input_lines):
        matrix[i] = list(line)
    return matrix


def one(input_name="one"):
    input_lines = list(lib.read("03", input_name, str.strip))
    matrix = read_matrix(input_lines)
    value, opposite = common(matrix)
    value = bin_array_to_int(value)
    opposite = bin_array_to_int(opposite)
    return value * opposite


def two(input_name="one"):
    input_lines = list(lib.read("03", input_name, str.strip))
    matrix = read_matrix(input_lines)

    remaining = matrix
    i = 0
    while remaining.shape[0] > 1:
        most_common, _ = common(remaining)
        remaining = remaining[remaining[:, i] == most_common[i]]
        i += 1
    o2 = bin_array_to_int(remaining[0])

    remaining = matrix
    i = 0
    while remaining.shape[0] > 1:
        _, least_common = common(remaining)
        remaining = remaining[remaining[:, i] == least_common[i]]
        i += 1
    co2 = bin_array_to_int(remaining[0])

    return co2 * o2
