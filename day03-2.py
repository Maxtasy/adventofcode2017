#https://adventofcode.com/2017/day/3


def part2(input_file):
	with open(input_file, "r") as f:
		number = int(f.read())

	spiral = {}
	spiral[(0,0)] = 1

	NEIGHBORS = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
	DIRECTION = [(1,0), (0,1), (-1,0), (0,-1)] #Right Up Left Down

	spiral = {}               # Spiral dictionary
	spiral[(0,0)] = 1
	x,y = 0,0
	steps_in_row = 1          # times spiral extends in same direction
	second_direction = False  # spiral extends in same direction twice: False if first leg, True if second
	nstep = 0                 # number of steps in current direction
	step_direction = 0        # index of direction in DIRECTION
	
	while True:
		dx, dy = DIRECTION[step_direction]
		x, y = x + dx, y + dy
		total = 0
		for neighbor in NEIGHBORS:
			nx, ny = neighbor
			if (x+nx, y+ny) in spiral:
				total += spiral[(x+nx, y+ny)]
		
		if total > number:
			return total
		spiral[(x,y)] = total
		nstep += 1
		if nstep == steps_in_row:
			nstep = 0
			step_direction = (step_direction + 1)% 4
			if second_direction:
				second_direction = False
				steps_in_row += 1
			else:
				second_direction = True


def main():
	input_file = "day03-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()