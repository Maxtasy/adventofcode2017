#https://adventofcode.com/2017/day/16


def part1(input_file):
	def spin(progs, num):
		progs_new = []
		progs_new.extend(progs[-int(num):])
		progs_new.extend(progs[:-int(num)])
		return progs_new

	def exchange(progs, num1, num2):
		temp = progs[int(num1)]
		progs[int(num1)] = progs[int(num2)]
		progs[int(num2)] = temp
		return progs

	def partner(progs, a, b):
		for i in range(len(progs)):
			if progs[i] == a:
				pos1 = i
			elif progs[i] == b:
				pos2 = i
		progs[pos1] = b
		progs[pos2] = a
		return progs

	with open(input_file, "r") as f:
		sequence = f.read().strip().split(",")

	progs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]

	instructions = []
	for step in sequence:
		instruction = []
		move = step[0]
		if move == "s":
			num1 = step[1:]
			num2 = None
		else:
			sub_step = step[1:].split("/")
			num1 = sub_step[0]
			num2 = sub_step[1]
		instruction.append(move)
		instruction.append(num1)
		instruction.append(num2)
		instructions.append(instruction)

	for instruction in instructions:
		#print(progs)
		#print(instruction)
		if instruction[0] == "s":
			progs = spin(progs, instruction[1])
		elif instruction[0] == "x":
			progs = exchange(progs, instruction[1], instruction[2])
		elif instruction[0] == "p":
			progs = partner(progs, instruction[1], instruction[2])
		else:
			print("Invalid instruction.")
			break

	final_str = ""

	for prog in progs:
		final_str += prog

	return final_str


def main():
	input_file = "day16-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()