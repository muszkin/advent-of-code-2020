from collections import defaultdict, deque


def parse_input(d: list):
    rules = [[y.strip() for y in x.split('contain')] for x in d]
    g = {' '.join(x[0].split()[:-1]): x[1:] for x in rules}
    for k, v in g.items():
        g[k] = {' '.join(s[2:].split()[:-1]): int(s[0]) for s in v[0].split(', ') if s != 'no other bags.'}
    return g


def create_reverse_graph(g):
    rev = defaultdict(list)
    for k, v in g.items():
        for new_key in v.keys():
            rev[new_key].append(k)
    return rev


def part_one(rev):
    q = deque(rev['shiny gold'])
    seen = {'shiny gold'}
    while q:
        cur = q.popleft()
        if cur not in seen:
            q += deque(rev[cur])
            seen.add(cur)
    return len(seen) - 1


def part_two(g):
    def dfs(g, bag):
        if not g[bag]:
            return 1
        return 1 + sum((v * dfs(g, k)) for k, v in g[bag].items())

    return dfs(g, 'shiny gold') - 1


file = open('day7-input.txt', 'r')
data = file.read().split('\n')
graph = parse_input(data)
rev_graph = create_reverse_graph(graph)

print(part_one(rev_graph))
print(part_two(graph))
