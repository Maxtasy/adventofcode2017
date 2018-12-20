#https://adventofcode.com/2017/day/24


from collections import defaultdict


def part1(input_file):
	with open(input_file, "r") as f:
		stream = f.read()

	def gen_bridges(bridge, components):
		bridge = bridge or [(0, 0)]
		cur = bridge[-1][1]
		for b in components[cur]:
			if not ((cur, b) in bridge or (b, cur) in bridge):
				new = bridge+[(cur, b)]
				yield new
				yield from gen_bridges(new, components)

	def parse_components(stream):
		components = defaultdict(set)
		for l in stream.strip().splitlines():
			a, b = [int(x) for x in l.split('/')]
			components[a].add(b)
			components[b].add(a)
		return components

	def solve(stream):
		components = parse_components(stream)
		mx = []
		for bridge in gen_bridges(None, components):
			mx.append((len(bridge), sum(a+b for a, b in bridge)))
		return mx

	solution = solve(stream)
	part1 = sorted(solution, key=lambda x: x[1])[-1][1]
	part2 = sorted(solution)[-1][1]

	return part1


def main():
	input_file = "day24-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()