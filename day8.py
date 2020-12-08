def run_program(instructions):
    accumulator = 0
    position = 0
    seen_instructions = set([])
    while position < len(instructions):
        if position in seen_instructions:
            return accumulator, position
        seen_instructions.add(position)
        instruction, value = instructions[position].split()
        value = int(value)

        if instruction == 'acc':
            accumulator += value
        elif instruction == 'jmp':
            position += value
            continue
        position += 1
    return accumulator, None


file = open("day8-input.txt", "r")

instructions_raw = file.read().splitlines()

print(run_program(instructions_raw)[0])

for i in range(len(instructions_raw)):
    program = instructions_raw.copy()
    end = 0
    if 'nop' in instructions_raw[i]:
        program[i] = instructions_raw[i].replace('nop', 'jmp')
        result, end = run_program(program)
    elif 'jmp' in instructions_raw[i]:
        program[i] = instructions_raw[i].replace('jmp', 'nop')
        result, end = run_program(program)
    if end is None:
        break

print(result)