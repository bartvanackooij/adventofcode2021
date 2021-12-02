def get_input(filename):
    with open(filename) as f:
        return [str(x.strip()) for x in f.read().split("\n")]


data = get_input("input.txt")


def puzzle1():
    forward = 0
    depth = 0
    for direc_steps in data:
        direc = direc_steps[:1]
        steps = int(direc_steps[-1])
        if direc == "f":
            forward += steps
        elif direc == "d":
            depth += steps
        elif direc == "u":
            depth -= steps
    return forward*depth


def puzzle2():
    forward = 0
    depth = 0
    aim = 0

    for direc_steps in data:
        direc = direc_steps[:1]
        steps = int(direc_steps[-1])
        if direc == "f":
            forward += steps
            depth += (aim * steps)
        elif direc == "d":
            aim += steps
        elif direc == "u":
            aim -= steps
    return forward*depth


print("puzzle 1: ", puzzle1())
print("puzzle 2: ", puzzle2())

