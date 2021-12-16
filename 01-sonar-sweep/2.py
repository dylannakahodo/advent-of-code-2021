with open("input", "r") as f:
    lines = f.readlines()
    lines = [int(l.strip("\n")) for l in lines]

answer = sum(x < y for x,y in zip(lines, lines[3:]))

print(answer)
