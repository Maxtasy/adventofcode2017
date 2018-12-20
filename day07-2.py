#https://adventofcode.com/2017/day/7


from collections import Counter


def part2(input_file):
	with open(input_file, "r") as f:
		lines = f.readlines()

	def build_dictionaries(lines):
		tower_list = []
		tower_self_weight = {}
		tower_total_weight = {}
		tower_children = {}
		
		for line in lines:
			line_items = line.replace(',', '').replace('(', '').replace(')', '').split()
			tower_name = line_items[0]
			self_weight = int(line_items[1])
			tower_list.append(tower_name)
			tower_self_weight[tower_name] = self_weight
			children = []
			if len(line_items) > 2:
				for i in range(3, len(line_items)):
					children.append(line_items[i])
			tower_children[tower_name] = children
		
		for tower in tower_list:
			tower_total_weight[tower] = calculate_tower_total_weight(tower, tower_self_weight, tower_children)
			
		return tower_list, tower_self_weight, tower_total_weight, tower_children

	def calculate_tower_total_weight(tower_name, tower_self_weight, tower_children):
		if not tower_children[tower_name]:
			return tower_self_weight[tower_name]
		else:
			tower_total_weight = tower_self_weight[tower_name]
			for tower_child in tower_children[tower_name]:
				tower_total_weight += calculate_tower_total_weight(tower_child, tower_self_weight, tower_children)
			return tower_total_weight

	tower_list, tower_self_weight, tower_total_weight, tower_children = build_dictionaries(lines)

	#base_tower = "gynfwly"
	#base_tower = "jjjks"
	base_tower = "gtervu"
	#base_tower = "ycbgx"

	def find_wrong_value_in_children(base_tower):
		weights = []
		for tower_child in tower_children[base_tower]:
			weights.append(tower_total_weight[tower_child])
		counter = Counter(weights)
		try:
			if min(counter, key=counter.get) != max(counter, key=counter.get):
				wrong_value_pos = weights.index(min(counter, key=counter.get))
				wrong_value = min(counter, key=counter.get)
				right_value = max(counter, key=counter.get)
				return tower_children[base_tower][wrong_value_pos], right_value - wrong_value
		except:
			return base_tower, 0
		return base_tower, 0

	#print(find_wrong_value_in_children(base_tower))
	return tower_self_weight[find_wrong_value_in_children(base_tower)[0]] + find_wrong_value_in_children(base_tower)[1]


def main():
	input_file = "day07-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()