#https://adventofcode.com/2017/day/1


def part2(input_file):
    with open(input_file, "r") as f:
        input_str = f.read()

    count = 0
    halfpoint = int(len(input_str) / 2)
    for i in range(len(input_str)):
        if i < halfpoint:
            if input_str[i] == input_str[i + halfpoint]:
                count += int(input_str[i])
        else:
            if input_str[i] == input_str[i - halfpoint]:
                count += int(input_str[i])
            
    return count


def main():
    input_file = "day01-input.txt"
    print(part2(input_file))


if __name__ == "__main__":
    main()