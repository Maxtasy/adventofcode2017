#https://adventofcode.com/2017/day/19


def part1(input_file):
	with open(input_file, "r") as f:
		lines = f.readlines()

	maze = {}

	for i in range(len(lines)):
		for j in range(201):
			maze[(j, i)] = lines[i][j]
		
	directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

	x_pos = 77
	y_pos = 0
	x_dir = 0
	y_dir = 1
	letters = []
	last = None

	while True:
		if maze.get((x_pos, y_pos)) == None:
			#print("Something went wrong.")
			break
		elif maze.get((x_pos, y_pos)) in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			letters.append(maze[(x_pos, y_pos)])
			if maze.get((x_pos + x_dir, y_pos + y_dir)) == " ":
				#print("Reached end.")
				break
		elif maze.get((x_pos, y_pos)) == "+":
			if maze.get((x_pos + x_dir, y_pos + y_dir)) != last:
				if last == "|":
					if maze[(x_pos + 1, y_pos)] == "-":
						x_dir = 1
						y_dir = 0
					elif maze[(x_pos - 1, y_pos)] == "-":
						x_dir = -1
						y_dir = 0
					elif maze[(x_pos, y_pos + 1)] == "-":
						x_dir = 0
						y_dir = 1
					elif maze[(x_pos, y_pos - 1)] == "-":
						x_dir = 0
						y_dir = -1
					else:
						#print("Reached end.")
						break
				elif last == "-":
					if maze[(x_pos + 1, y_pos)] == "|":
						x_dir = 1
						y_dir = 0
					elif maze[(x_pos - 1, y_pos)] == "|":
						x_dir = -1
						y_dir = 0
					elif maze[(x_pos, y_pos + 1)] == "|":
						x_dir = 0
						y_dir = 1
					elif maze[(x_pos, y_pos - 1)] == "|":
						x_dir = 0
						y_dir = -1
					else:
						#print("Reached end.")
						break
		last = maze[(x_pos, y_pos)]
		x_pos += x_dir
		y_pos += y_dir
			
	return "".join(letters)


def main():
	input_file = "day19-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()