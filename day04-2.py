#https://adventofcode.com/2017/day/4


def part2(input_file):
	with open(input_file, "r") as f:
		lines = f.readlines()

	count = 0
	for line in lines:
		s = line.split()
		if len(s) == len(set(s)):
			count += 1

	return count


def main():
	input_file = "day04-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()