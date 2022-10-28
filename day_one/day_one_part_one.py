def day_one_solution():
    input = []
    with open('day_one/input.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            input.append(int(line.strip()))
    res = 0
    for i in range(1, len(input)):
        if input[i] > input[i-1]:
            res += 1
    return res
    
print(day_one_solution())
## Output is 1681