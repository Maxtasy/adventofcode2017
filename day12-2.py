#https://adventofcode.com/2017/day/12


def part2(input_file):
	def build_dict_and_program_list(lines):
		d = {}
		prog_list = []
		for line in lines:
			line = line.strip("\n").replace(" ", "").split("<->")
			prog_list.append(line[0])
			d[line[0]] = line[1].split(",")

		return d, prog_list

	def get_group(d, main_program):
		group = []
		group.append(main_program)
		group = list(set(group + d[main_program]))
		
		while True:
			old_size = len(group)
			for program in group:
				group = list(set(group + d[program]))
			if old_size == len(group):
				break

		return group

	def count_groups(d, prog_list):
		tested = []
		num_groups = 0
		for program in prog_list:
			if program not in tested:
				tested += get_group(d, program)
				num_groups += 1
		return num_groups

	with open(input_file, "r") as f:
		lines = f.readlines()

	d, prog_list = build_dict_and_program_list(lines)

	return count_groups(d, prog_list)


def main():
	input_file = "day12-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()