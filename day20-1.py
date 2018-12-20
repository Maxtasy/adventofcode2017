#https://adventofcode.com/2017/day/20


def part1(input_file):
	with open(input_file, "r") as f:
		lines = f.readlines()

	particles = []
	distances = []

	for line in lines:
		p = []
		line = line.split(",")
		p.append(int(line[0][3:]))
		p.append(int(line[1]))
		p.append(int(line[2].replace(">", "")))
		p.append(int(line[3][4:]))
		p.append(int(line[4]))
		p.append(int(line[5].replace(">", "")))
		p.append(int(line[6][4:]))
		p.append(int(line[7]))
		p.append(int(line[8].replace(">\n", "")))
		distances.append(None)
		particles.append(p)

	while True:
		for i in range(len(particles)):
			particles[i][3] += particles[i][6]
			particles[i][4] += particles[i][7]
			particles[i][5] += particles[i][8]
			particles[i][0] += particles[i][3]
			particles[i][1] += particles[i][4]
			particles[i][2] += particles[i][5]
			distances[i] = abs(particles[i][0]) + abs(particles[i][1]) + abs(particles[i][2])
		print(min(distances), distances.index(min(distances)))


def main():
	input_file = "day20-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()