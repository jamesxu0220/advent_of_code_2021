from day_one_part_one import get_input

def day_one_solution_two():
    input = get_input()
    res = 0
    cur_sum = sum(input[:3])
    for i in range(3, len(input)):
        new_sum = cur_sum - input[i-3] + input[i]
        if new_sum > cur_sum:
            res += 1
        cur_sum = new_sum
    return res
    
# print(day_one_solution_two())
# Output is 1704