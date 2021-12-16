# https://adventofcode.com/2021/day/1

with open("test.txt", "r") as f:
    lines = f.readlines()
    lines = [int(l.strip("\n")) for l in lines]

with open("input", "r") as f:
    lines = f.readlines()
    lines = [int(l.strip("\n")) for l in lines]

answer = sum(x < y for x,y in zip(lines, lines[1:]))

print(answer)


