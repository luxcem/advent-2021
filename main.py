#!/usr/bin/env python3
import sys
import importlib

if __name__ == "__main__":
    day = sys.argv[1]
    puzzle = sys.argv[2] if len(sys.argv) > 2 else "one"
    module = f"day{day}"
    my_module = importlib.import_module(module)

    solution = getattr(my_module, puzzle)
    value = solution(*sys.argv[3:])
    print(value)
