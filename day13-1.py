#https://adventofcode.com/2017/day/13


def part1(input_file):
	def calculate_severity(d):
		current_layer = -1
		detections = 0
		total_severity = 0
		#Loop until we are through all layers
		while current_layer < 89:
			#print("Next layer.")
			#Move self
			current_layer += 1
			#Is hit?
			if d.get(current_layer):
				#print("On active layer (" + str(current_layer) + "). Checking if hit...")
				#print("Position of scanner on current layer: " + str(d.get(current_layer)[1]))
				if d.get(current_layer)[1] == 1:
					#print("Hit detected. Calculating severity...")
					#Calculate severity points
					detections += 1
					severity = current_layer * d[current_layer][0]
					#Add severity points
					total_severity += severity
					#print("Severity of " + str(severity) + " added. Total severity: " + str(total_severity))
			#Move scanners
			for scanner in d:
				if d[scanner][1] + d[scanner][2] > d[scanner][0]:
					d[scanner][2] = -1
				elif d[scanner][1] + d[scanner][2] < 1:
					d[scanner][2] = 1
				d[scanner][1] += d[scanner][2]
		
		return total_severity, detections

	with open(input_file, "r") as f:
		lines = f.readlines()

	#Build dictionary - depth: range, scanner pos, scanner dir (1 = down, -1 = up)
	d = {}
	for line in lines:
		layer_properties = []
		line = line.strip("\n").split(": ")
		layer_properties.append(int(line[1]))
		layer_properties.append(1)
		layer_properties.append(1)
		d[int(line[0])] = layer_properties

	return calculate_severity(d)[0]


def main():
	input_file = "day13-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()