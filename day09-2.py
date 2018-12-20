#https://adventofcode.com/2017/day/9


import re


def part2(input_file):
	with open(input_file, "r") as f:
		s = f.read()

	#print original stream
	#print(s)

	#remove escaped stuff
	escaped_regex = re.compile(r"""!.""")
	s = escaped_regex.sub("", s)
	length_after_removing_escaped = len(s)

	#remove_garbage
	garbage_regex = re.compile(r"""<.*?>""")

	#count all regex hits
	garbage_parts = len(garbage_regex.findall(s))

	s = garbage_regex.sub("", s)

	length_after_removing_garbage = len(s)
	#remove commas
	s = s.replace(",", "")

	return length_after_removing_escaped - length_after_removing_garbage - garbage_parts * 2


def main():
	input_file = "day09-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()