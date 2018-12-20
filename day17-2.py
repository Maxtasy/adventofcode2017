#https://adventofcode.com/2017/day/17


def part2(input_file):
	index = 0
	steps = 377
	n = 0

	for i in range(1, 50000001):
		index = (index + steps) % i
		
		if index == 0:
			n = i
		index += 1

	return n


def main():
	input_file = "day17-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()