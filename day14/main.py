#!/usr/bin/env python3

import lib
from collections import Counter


def step(bigrams, reactions):
    new_bigrams = Counter()
    for bigram, count in bigrams.items():
        if bigram in reactions.keys():
            new_bigrams[bigram[0] + reactions[bigram]] += count
            new_bigrams[reactions[bigram] + bigram[1]] += count
    return new_bigrams


def one(input_name="one", n=10):
    input_lines = lib.read("14", input_name)
    chain = input_lines[0]
    reactions = {r[0]: r[1] for r in map(lambda x: x.split(" -> "), input_lines[2:])}
    bigrams = Counter([chain[i : i + 2] for i in range(len(chain) - 1)])
    for i in range(n):
        bigrams = step(bigrams, reactions)

    # Count letters (first letter of each bigram + last element of input chain)
    counter = Counter()
    for bigram, count in bigrams.items():
        counter[bigram[0]] += count
    counter[chain[-1]] += 1
    return max(counter.values()) - min(counter.values())


def two(input_name="one"):
    return one(input_name, 40)
