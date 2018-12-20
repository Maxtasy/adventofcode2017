#https://adventofcode.com/2017/day/3


import math


def part1(input_file):
	with open(input_file, "r") as f:
		number = int(f.read())
	upper = math.ceil(number**.5)
	if upper %2 == 0:
		upper += 1

	return upper ** 2 - number


def main():
	input_file = "day03-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()