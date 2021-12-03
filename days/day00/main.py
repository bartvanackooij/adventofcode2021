import os
import sys

sys.path.insert(1, (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + "/utils"))

import util


def get_input(filename):
    with open(filename) as f:
        return [str(x.strip()) for x in f.read().split("\n")]


def puzzle1():
    return ""


def puzzle2():
    return ""


print("puzzle 1: ", puzzle1())
print("puzzle 2: ", puzzle2())

