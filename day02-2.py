#https://adventofcode.com/2017/day/2


def part2(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        s = line.split()
        s = list(map(int, s))
        for num in s:
            for i in range(len(s)):
                if num != s[i] and num % s[i] == 0:
                    count += int(num / s[i])

    return count


def main():
    input_file = "day02-input.txt"
    print(part2(input_file))


if __name__ == "__main__":
    main()