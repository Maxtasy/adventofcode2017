#https://adventofcode.com/2017/day/21


def part1(input_file):
	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")

	rules = {}
	for line in lines:
		i, o = line.split(" => ")
		i = tuple([tuple(s) for s in i.split('/')])
		o = tuple([tuple(s) for s in o.split('/')])

		n = len(i)
		def new_coords(r, c, flipped, reverse_r, reverse_c):
			if reverse_r:
				r = n-1-r
			if reverse_c:
				c = n-1-c
			if flipped:
				r,c = c,r
			return i[r][c]
		for flipped in [True,False]:
			for reverse_r in [True,False]:
				for reverse_c in [True,False]:
					ii = tuple([tuple(new_coords(r,c,flipped,reverse_r,reverse_c) for c in range(n)) for r in range(n)])
					rules[ii] = o

	pattern = [list('.#.'), list('..#'), list('###')]

	for t in range(6):
		n = len(pattern)

		ans = 0
		for r in range(n):
			for c in range(n):
				if pattern[r][c] == '#':
					ans += 1
		print(t, ans)

		if n%2==0:
			block_size = 2
		else:
			block_size = 3
		assert n%block_size == 0
		new_blocks = []
		for r in range(n//block_size):
			block_row = []
			for c in range(n//block_size):
				block_in = tuple([tuple([pattern[r*block_size+rr][c*block_size+cc] for cc in range(block_size)]) for rr in range(block_size)])
				block_row.append(rules[block_in])
			new_blocks.append(block_row)
		new_n = n//block_size*(block_size+1)
		def from_block(r,c):
			r0, r1 = r//(block_size+1), r%(block_size+1)
			c0, c1 = c//(block_size+1), c%(block_size+1)
			return new_blocks[r0][c0][r1][c1]
		new_pattern = [[from_block(r,c) for c in range(new_n)] for r in range(new_n)]
		pattern = new_pattern


def main():
	input_file = "day21-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()