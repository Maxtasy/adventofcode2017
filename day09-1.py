#https://adventofcode.com/2017/day/9


import re


def part1(input_file):
    with open(input_file, "r") as f:
        s = f.read()

    #remove escaped stuff
    escaped_regex = re.compile(r"""!.""")
    s = escaped_regex.sub("", s)
    #remove_garbage
    garbage_regex = re.compile(r"""<.*?>""")
    s = garbage_regex.sub("", s)
    s = s.replace(",", "")
            
    #check if same amount of open and close brackets
    open_count = 0
    close_count = 0

    for c in s:
        if c == "{":
            open_count += 1
        elif c == "}":
            close_count += 1

    #calculate value of whole stream
    total_value = 0
    value_rating = 0
    for i in range(len(s)):
        if s[i] == "{":
            value_rating += 1
        elif s[i] == "}":
            total_value += value_rating
            value_rating -= 1
    
    return total_value


def main():
    input_file = "day09-input.txt"
    print(part1(input_file))


if __name__ == "__main__":
    main()