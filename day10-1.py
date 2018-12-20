#https://adventofcode.com/2017/day/10


def part1(input_file):
	def solve(sequence):
		l = list(range(256))
		pos = 0
		skip = 0
		for length in sequence:
			for i in range(length // 2):
				temp = l[(pos + i) % 256]
				l[(pos + i) % 256] = l[(pos + length - 1 - i) % 256]
				l[(pos + length - 1 - i) % 256] = temp
			pos = (pos + length + skip) % 256
			skip += 1

		return l[0] * l[1]

	with open(input_file, "r") as f:
		stream = f.read().strip("\n")

	sequence = stream.split(",")
	sequence = list(map(int, sequence))

	return solve(sequence)


def main():
	input_file = "day10-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()