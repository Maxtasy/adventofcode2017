#https://adventofcode.com/2017/day/11


def part2(input_file):
	with open(input_file, "r") as f:
		sequence = f.read().strip().split(",")

	#pos as x, y, z
	pos = [0, 0, 0]
	furthest = 0
	for move in sequence:
		if move == "n":
			pos[1] += 1
			pos[2] -= 1
		elif move == "ne":
			pos[0] += 1
			pos[2] -= 1
		elif move == "nw":
			pos[0] -= 1
			pos[1] += 1
		elif move == "s":
			pos[1] -= 1
			pos[2] += 1
		elif move == "se":
			pos[0] += 1
			pos[1] -= 1
		elif move == "sw":
			pos[0] -= 1
			pos[2] += 1
		else:
			print("Invalid move.")
			return None
		if abs(pos[2]) > furthest:
			furthest = abs(pos[2])
	return furthest


def main():
	input_file = "day11-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()