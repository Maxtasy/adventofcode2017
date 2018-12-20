#https://adventofcode.com/2017/day/5


def part2(input_file):
	with open(input_file, "r") as f:
		l = f.read()

	l = l.split()
	l = list(map(int, l))

	steps = 0
	index = 0

	while index < len(l):
		if l[index] >= 3:
			new_index = index + l[index]
			l[index] -= 1
		else:
			new_index = index + l[index]
			l[index] += 1
		index = new_index
		steps += 1

	return steps


def main():
	input_file = "day05-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()