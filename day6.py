def get_same_yes_for_group(g: list):
    yes_sets = []
    for answers in g:
        set_of_answers = set()
        for a in answers:
            set_of_answers.add(a)
        yes_sets.append(set_of_answers)
    if len(yes_sets) == 1:
        return len(yes_sets[0])
    else:
        return len(yes_sets[0].intersection(*yes_sets[1:]))


def get_answer_for_group(g: str):
    yes_answers = set()
    for answer in g:
        yes_answers.add(answer)
    return len(yes_answers)


file = open("day6-input.txt", "r")

groups = file.read().split("\n\n")

yes_count = 0
for group in groups:
    yes_count += get_answer_for_group(group.replace("\n", ""))

print(yes_count)

yes_count = 0
for group in groups:
    yes_count += get_same_yes_for_group(group.split("\n"))

print(yes_count)
