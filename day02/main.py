#!/usr/bin/env python3

import lib


def one(input_name="one"):
    input_lines = lib.read("02", input_name, str.strip)
    x = 0
    z = 0
    for line in input_lines:
        command, value = line.split(" ")
        value = int(value)
        if command == "forward":
            x += value
        elif command == "down":
            z += value
        elif command == "up":
            z -= value
    return x * z


def two(input_name="one"):
    input_lines = lib.read("02", input_name, str.strip)
    x = 0
    z = 0
    aim = 0
    for line in input_lines:
        command, value = line.split(" ")
        value = int(value)
        if command == "forward":
            x += value
            z += aim * value
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value
    return x * z
