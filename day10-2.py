#https://adventofcode.com/2017/day/10


from functools import reduce


def part2(input_file):
	with open(input_file, "r") as f:
		stream = f.read().strip()
	lens = [ord(x) for x in stream]
	lens.extend([17,31,73,47,23])
	nums = [x for x in range(0,256)]
	pos = 0
	skip = 0
	for _ in range(64):
		for l in lens:
			to_reverse = []
			for x in range(l):
				n = (pos + x) % 256
				to_reverse.append(nums[n])
			to_reverse.reverse()
			for x in range(l):
				n = (pos + x) % 256
				nums[n] = to_reverse[x]
			pos += l + skip
			pos = pos % 256
			skip += 1
	dense = []
	for x in range(0,16):
		subslice = nums[16*x:16*x+16]
		dense.append('%02x'%reduce((lambda x,y: x ^ y),subslice))
	return ''.join(dense)


def main():
	input_file = "day10-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()