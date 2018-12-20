#https://adventofcode.com/2017/day/1


def part1(input_file):
	with open(input_file, "r") as f:
		input_str = f.read()

	count = 0
	for i in range(len(input_str)):
		if input_str[i] == input_str[i - 1]:
			count += int(input_str[i])
			
	return count


def main():
	input_file = "day01-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()