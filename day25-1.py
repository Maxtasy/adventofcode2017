#https://adventofcode.com/2017/day/25


def part1(input_file):
	# I did the rules manually, not from input_file
	# with open(input_file, "r") as f:
	# 	stream = f.read()

	d = {}

	pos = 0
	state = "A"

	steps = 12964419

	for i in range(steps):
		if d.get(pos) == None:
				d[pos] = 0
		
		if state == "A":
			if d[pos] == 0:
				d[pos] = 1
				state = "B"
			else:
				d[pos] = 0
				state = "F"
			pos += 1
		elif state == "B":
			if d[pos] == 1:
				state = "C"
			pos -= 1
		elif state == "C":
			if d[pos] == 0:
				d[pos] = 1
				pos -= 1
				state = "D"
			else:
				d[pos] = 0
				pos += 1
		elif state == "D":
			if d[pos] == 0:
				d[pos] = 1
				pos -= 1
				state = "E"
			else:
				pos += 1
				state = "A"
		elif state == "E":
			if d[pos] == 0:
				d[pos] = 1
				state = "F"
			else:
				d[pos] = 0
				state = "D"
			pos -= 1
		elif state == "F":
			if d[pos] == 0:
				d[pos] = 1
				pos += 1
				state = "A"
			else:
				d[pos] = 0
				pos -= 1
				state = "E"
		
		steps += 1

	count = 0

	for value in d.values():
		if value == 1:
			count += 1

	return count


def main():
	input_file = "day25-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()