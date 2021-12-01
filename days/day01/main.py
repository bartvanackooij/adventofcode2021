with open("input.txt") as file:
    data = [int(line) for line in file]


def puzzle1():
    answer1_count = 0
    for x in range(len(data)-1):
        if data[x] < data[x+1]:
            answer1_count += 1
    return answer1_count


def puzzle2():
    answer2_count = 0
    for x in range(len(data)-3):
        # tmw = three-measurement window
        tmw = 0
        tmw2 = 0
        for y in range(3):
            tmw += data[(x+y)]
            tmw2 += data[x+1+y]
        if tmw < tmw2:
            answer2_count += 1
    return answer2_count


print("puzzle 1: ", puzzle1())
print("puzzle 2: ", puzzle2())

