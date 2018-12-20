#https://adventofcode.com/2017/day/14


def part1(input_file):
	def create_knot_hash(hash_input, suffix = [17, 31, 73, 47, 23]):
		sequence = []
		for c in hash_input:
			sequence.append(ord(c))
		
		sequence += suffix
		
		pos = 0
		skip = 0
		sparse = list(range(256))
		for i in range(64):
			for length in sequence:
				for i in range(length // 2):
					temp = sparse[(pos + i) % 256]
					sparse[(pos + i) % 256] = sparse[(pos + length - 1 - i) % 256]
					sparse[(pos + length - 1 - i) % 256] = temp
				pos = (pos + length + skip) % 256
				skip += 1
		
		dense = []
		index = 0
		
		for _ in range(16):
			xor = 0
			for i in range(16):
				xor ^= sparse[index + i]
			dense.append(xor)
			index += 16
		
		knot_hash = ""
		
		for element in dense:
			h = hex(element)
			if len(h) < 4:
				hex_value = "0"+h[-1]
			else:
				hex_value = h[-2:]
			knot_hash += hex_value
		
		return knot_hash

	def convert_to_binary_string(knot_hash):
		binary_string = ""
		for c in knot_hash:
			binary_part = f'{int(c, 16):0004b}'
			binary_string += binary_part
		
		return binary_string

	with open(input_file, "r") as f:
		prefix = f.read()

	hash_inputs = []

	for i in range(128):
		hash_inputs.append(prefix + "-" + str(i))

	knot_hashes = []
	for hash_input in hash_inputs:
		knot_hashes.append(create_knot_hash(hash_input))

	#print(knot_hashes)

	binary_strings = []
	for knot_hash in knot_hashes:
		binary_strings.append(convert_to_binary_string(knot_hash))

	#print(binary_strings)

	count = 0

	for binary_string in binary_strings:
		for c in binary_string:
			if c == "1":
				count += 1

	return count


def main():
	input_file = "day14-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()