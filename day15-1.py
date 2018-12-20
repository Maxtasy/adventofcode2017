#https://adventofcode.com/2017/day/15


def part1(input_file):
	def gen_next(gen, num):
		if gen == "a":
			factor = 16807
		elif gen == "b":
			factor = 48271
		else:
			return False
		return (num*factor) % 2147483647

	def make_bin(num):
		part = str(bin(num)[2:])
		zeros = 32 - len(part)
		
		return str(zeros * "0") + part

	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")

	a = int(lines[0].split()[-1]) #634
	b = int(lines[1].split()[-1]) #301

	score = 0

	for i in range(40000000):
		a = gen_next("a", a)
		a_bin = make_bin(a)
		
		b = gen_next("b", b)
		b_bin = make_bin(b)
		
		if a_bin[16:] == b_bin[16:]:
			score += 1

	return score


def main():
	input_file = "day15-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()