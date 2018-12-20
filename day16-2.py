#https://adventofcode.com/2017/day/16


def part2(input_file):
	with open(input_file, "r") as f:
		sequence = f.read().strip().split(",")

	progs = list("abcdefghijklmnop")

	def dance(reps, progs):
		seen = []
		for i in range(reps):
			s = ''.join(progs)
			if s in seen:  # cycles are short; no runtime lost for comparing full list instead of s == seen[0]
				print(seen[reps % i])
				return progs
			seen.append(s)

			for move in sequence:
				if move[0] == 's':
					i = int(move[1:])
					progs = progs[-i:] + progs[:-i]
				else:
					if move[0] == 'x':
						a,b = map(int, move[1:].split('/'))
						progs[a], progs[b] = progs[b], progs[a]
					if move[0] == 'p':
						a,b = move[1:].split('/')
						A = progs.index(a)
						B = progs.index(b)
						progs[A], progs[B] = progs[B], progs[A]

		return ''.join(progs)  # if no cycle - part 1

	dance(1000000000, progs[:])


def main():
	input_file = "day16-input.txt"
	part2(input_file)


if __name__ == "__main__":
	main()