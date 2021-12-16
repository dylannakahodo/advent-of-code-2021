with open("input", "r") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

x_pos = 0
depth = 0
aim = 0

for command in lines:
    direction, value = command.split()
    value = int(value)
    
    if direction == "forward":
        x_pos += value
        depth += aim * value
    elif direction == "down":
        aim += value
    elif direction == "up":
        aim -= value
    else:
        print("Unknown direction! Exiting")
        exit(-1)

answer = x_pos * depth
print(answer)
    
