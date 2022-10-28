from day_two_part_one import get_input

def day_two_solution_two():
    input = get_input()
    horiz = 0
    depth = 0
    aim = 0
    for line in input:
        command, val = line.split(" ")
        if command == "forward":
            horiz += int(val)
            depth += int(val) * aim
        elif command == "up":
            aim -= int(val)
        else:
            aim += int(val)
    return horiz * depth

# print(day_two_solution_two())
# Output is 1975421260