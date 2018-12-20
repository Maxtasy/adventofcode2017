#https://adventofcode.com/2017/day/6


def part2(input_file):
	def find_largest_bank(l):
		largest = 0
		index = 0
		for i in range(len(l)):
			if l[i] > largest:
				largest = l[i]
				index = i
		return largest, index

	def distribute_blocks_and_return_list(l, largest, index):
		l[index] = 0
		for i in range(largest):
			if (index + 1) >= len(l):
				index = -1
			l[index + 1] += 1
			index += 1
		return l


	def num_of_cycles(l):
		pattern_collection = []
		cycles = 0
		while l not in pattern_collection:
			cycles += 1
			l_old = l[:]
			pattern_collection.append(l_old)
			largest, index = find_largest_bank(l)
			distribute_blocks_and_return_list(l, largest, index)
		return cycles, l

	with open(input_file, "r") as f:
		l = f.read()

	l = l.split()
	l = list(map(int, l))


	num_of_cycles(l)
	l_new = l[:]

	return num_of_cycles(l_new)


def main():
	input_file = "day06-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()