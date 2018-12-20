#https://adventofcode.com/2017/day/22


def part1(input_file):
	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")

	grid = {}
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			grid[(j, i)] = lines[i][j]

	directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

	x = 12
	y = 12
	d = (0, -1)
	count = 0

	for i in range(10000):
		if (x, y) not in grid.keys():
			grid[(x, y)] = "."
			
		if grid[(x, y)] == "#":
			grid[(x, y)] = "."
			d = directions[(directions.index(d) + 1) % 4]
		elif grid[(x, y)] == ".":
			grid[(x, y)] = "#"
			d = directions[(directions.index(d) - 1) % 4]
			count += 1
		x += d[0]
		y += d[1]
		
	return count


def main():
	input_file = "day22-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()