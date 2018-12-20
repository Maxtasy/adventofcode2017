#https://adventofcode.com/2017/day/7


def part1(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    words = []
    bad_words = []

    for line in lines:
        line_items = line.split()
        if "->" in line_items:
            for i in range(3, len(line_items)):
                bad_words.append(line_items[i].replace(',',''))
        words.append(line_items[0])
    starter_word = list(set(words) - set(bad_words))

    return starter_word[0]


def main():
    input_file = "day07-input.txt"
    print(part1(input_file))


if __name__ == "__main__":
    main()