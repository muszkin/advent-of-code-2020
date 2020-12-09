def has_pair(preamble_list: list, num: int):
    for n in preamble_list:
        if abs(num - n) in preamble_list:
            return True
    return False


def find_sum(nums, target_sum):
    run_sums = nums.copy()
    for runLength in range(2, len(nums)):
        run_sums.pop()
        for i in range(len(run_sums)):
            run_sums[i] += nums[i + runLength - 1]
            if run_sums[i] == target_sum:
                run = nums[i:i + runLength]
                return min(run) + max(run)


numbers = list(map(int, open("day9-input.txt", "r").read().split("\n")))
full_numbers = numbers.copy()

for index, number in enumerate(numbers[25:]):
    preamble = full_numbers[index:index+25]
    if has_pair(preamble, number):
        continue
    else:
        print(number)
        print(find_sum(full_numbers, number))
        break


