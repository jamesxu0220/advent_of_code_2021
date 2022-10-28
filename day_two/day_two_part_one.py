def get_input():
    input = []
    with open('day_two/input.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            input.append(line.strip())
    return input


def day_two_solution_one():
    input = get_input()
    horiz = 0
    depth = 0
    for line in input:
        command, val = line.split(" ")
        if command == "forward":
            horiz += int(val)
        elif command == "up":
            depth -= int(val)
        else:
            depth += int(val)
    return horiz * depth

# print(day_two_solution_one())
# Output is 1990000