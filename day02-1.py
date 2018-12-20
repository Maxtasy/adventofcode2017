#https://adventofcode.com/2017/day/2


def part1(input_file):
	with open(input_file, "r") as f:
		lines = f.readlines()

	count = 0
	for line in lines:
		s = line.split()
		s = list(map(int, s))
		count += max(s) - min(s)
		
	return count


def main():
	input_file = "day02-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()