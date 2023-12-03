from contextlib import suppress


def read_input():
    with open("day_3_input.txt") as file:
        return [line.rstrip() for line in file]

def get_numbers_from_input(input):
    numbers = []
    characters = ['/', '\\', '|', '-', '+', '-', '_', '*', '#', '@', '!',
                  '?', '>', '<', '^', 'v', '(', ')', '[', ']', '{', '}',
                  ':', ';', ',', '~', '.', '`', '$', '%', '&', '=', '"']
    for line in input:
        for char in characters:
            line = line.replace(char, ' ')
        line = line.split()
        numbers.append([int(x) for x in line if x != '' and x != ' '])
    return numbers

def char_condition(char):
    if not char.isdigit() and char != '.':
        return True
    return False

def check_valid_number(input, line_index, char_index):
    with suppress(Exception):
        if char_condition(input[line_index][char_index + 1]):
            return True
    with suppress(Exception):
        if char_condition(input[line_index][char_index -1]):
            return True
    with suppress(Exception):
        if char_condition(input[line_index - 1][char_index]):
            return True
    with suppress(Exception):
        if char_condition(input[line_index + 1][char_index]):
            return True
    with suppress(Exception):
        if char_condition(input[line_index + 1][char_index + 1]):
            return True
    with suppress(Exception):
        if char_condition(input[line_index + 1][char_index - 1]):
            return True
    with suppress(Exception):
        if char_condition(input[line_index - 1][char_index + 1]):
            return True
    with suppress(Exception):
        if char_condition(input[line_index - 1][char_index - 1]):
            return True
    return False

def get_valid_numbers(input, numbers):
    valid_numbers = []
    for i, line in enumerate(input):
        number_index = -1
        number_found = False
        number_valid = False
        for j, char in enumerate(line):
            if char.isdigit():
                if not number_found:
                    number_index += 1
                    number_found = True
            else:
                number_found = False
                number_valid = False
            if char.isdigit():
                if check_valid_number(input, i, j) and not number_valid:
                    number_valid = True
                    try:
                        valid_numbers.append(numbers[i][number_index])
                    except:
                        pass
    return valid_numbers

def main():
    input = read_input()
    numbers = get_numbers_from_input(input)
    valid_numbers = get_valid_numbers(input, numbers)
    print(sum(valid_numbers))


if __name__ == '__main__':
    main()