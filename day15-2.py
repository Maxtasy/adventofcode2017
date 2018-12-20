#https://adventofcode.com/2017/day/15


def part2(input_file):
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

	a_bin_l = []
	b_bin_l = []

	while len(b_bin_l) < 5000000:
		a = gen_next("a", a)
		if a % 4 == 0:
			a_bin_l.append(make_bin(a))
		
		b = gen_next("b", b)
		if b % 8 == 0:
			b_bin_l.append(make_bin(b))

	for i in range(len(b_bin_l)):
		if a_bin_l[i][16:] == b_bin_l[i][16:]:
			score += 1

	return score


def main():
	input_file = "day15-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()