#https://adventofcode.com/2017/day/23


import string


def part1(input_file):
	with open(input_file, "r") as f:
		instr_l = [line.strip("\n").split(" ") for line in f.readlines()]

	regs = {instr[1]: 0 for instr in instr_l if instr[1] in string.ascii_lowercase}

	index = 0
	count = 0

	while 0 <= index < len(instr_l):
		offset = 0
		
		cur_instr = instr_l[index]
		method = cur_instr[0]
		first = cur_instr[1]
		if len(cur_instr) > 2:
			second = cur_instr[2]
			if second in string.ascii_lowercase:
				second = int(regs[second])
			else:
				second = int(second)

		if method == "set":
			regs[first] = second
		elif method == "sub":
			regs[first] -= second
		elif method == "mul":
			regs[first] *= second
			count += 1
		elif method == "jnz":
			if first in string.ascii_lowercase:
				first = regs[first]
			if first != 0:
				offset = second - 1
		
		index += 1 + offset

	return count


def main():
	input_file = "day23-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()