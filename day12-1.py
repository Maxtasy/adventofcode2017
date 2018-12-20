#https://adventofcode.com/2017/day/12


def part1(input_file):
	def build_dict(lines):
		d = {}
		for line in lines:
			line = line.strip("\n").replace(" ", "").split("<->")
			d[line[0]] = line[1].split(",")

		return d

	def get_group_size(d, main_program):
		group = []
		group.append(main_program)
		group = list(set(group + d[main_program]))
		
		while True:
			old_size = len(group)
			for program in group:
				group = list(set(group + d[program]))
			if old_size == len(group):
				break

		return len(group)

	with open(input_file, "r") as f:
		lines = f.readlines()


	d = build_dict(lines)
	size = get_group_size(d, "0")

	return size


def main():
	input_file = "day12-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()