#https://adventofcode.com/2017/day/17


def part1(input_file):
	with open(input_file, "r") as f:
		steps = int(f.read())

	c_buf = [0]
	index = 0

	for i in range(1, 2018):
		index = (index + steps) % len(c_buf)
		c_buf.insert(index + 1, i)
		index += 1

	return c_buf[c_buf.index(2017) + 1]


def main():
	input_file = "day17-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()