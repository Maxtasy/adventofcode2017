#https://adventofcode.com/2017/day/8


def part1(input_file):
	def parse_input(lines):
		register_values = {}
		instruction_list = []
		
		for line in lines:
			instruction_line = []
			line_items = line.split()
			register_name = line_items[0]
			instruction = line_items[1]
			instruction_value = int(line_items[2])
			condition = [line_items[4], line_items[5], int(line_items[6])]
			instruction_line.append(register_name)
			instruction_line.append(instruction)
			instruction_line.append(instruction_value)
			instruction_line.append(condition)
			instruction_list.append(instruction_line)
			if register_name not in register_values:
				register_values[register_name] = 0
		
		return register_values, instruction_list
		
	def execute_instruction_list(register_values, instruction_list):
		for instruction_line in instruction_list:
			condition_met = False
			if ">" in instruction_line[3]:
				if register_values[instruction_line[3][0]] > instruction_line[3][2]:
					condition_met = True
			elif ">=" in instruction_line[3]:
				if register_values[instruction_line[3][0]] >= instruction_line[3][2]:
					condition_met = True
			elif "<" in instruction_line[3]:
				if register_values[instruction_line[3][0]] < instruction_line[3][2]:
					condition_met = True
			elif "<=" in instruction_line[3]:
				if register_values[instruction_line[3][0]] <= instruction_line[3][2]:
					condition_met = True
			elif "==" in instruction_line[3]:
				if register_values[instruction_line[3][0]] == instruction_line[3][2]:
					condition_met = True
			elif "!=" in instruction_line[3]:
				if register_values[instruction_line[3][0]] != instruction_line[3][2]:
					condition_met = True
			if condition_met:
				if instruction_line[1] == "inc":
					register_values[instruction_line[0]] += instruction_line[2]
				elif instruction_line[1] == "dec":
					register_values[instruction_line[0]] -= instruction_line[2]

	with open(input_file, "r") as f:
		lines = f.readlines()

	register_values, instruction_list = parse_input(lines)
	execute_instruction_list(register_values, instruction_list)
	return max(list(register_values.values()))


def main():
    input_file = "day08-input.txt"
    print(part1(input_file))


if __name__ == "__main__":
    main()