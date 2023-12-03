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
    if char.isdigit():
        return True
    return False

def get_number_index(line, line_index, char_index, numbers):
    number_index = -1
    number_found = False
    for j, char in enumerate(line):
        if char.isdigit():
            if not number_found:
                number_index += 1
                number_found = True
        else:
            number_found = False
        if j == char_index:
            return numbers[line_index][number_index]
    return None

def get_gear_adjacent_number_indexes(input, line_index, char_index, numbers):
    adjacent_number_indexes = []
    number_found = [
        [False, False, False],
        [False, None, False],
        [False, False, False]
    ]
    # up
    with suppress(Exception):
        if char_condition(input[line_index-1][char_index -1]):
            number = get_number_index(input[line_index - 1], line_index - 1, char_index -1, numbers)
            if number:
                adjacent_number_indexes.append(number)
                number_found[0][0] = True
    with suppress(Exception):
        if char_condition(input[line_index - 1][char_index]):
            number = get_number_index(input[line_index - 1], line_index - 1, char_index, numbers)
            if number:
                if not number_found[0][0]:
                    adjacent_number_indexes.append(number)
                number_found[0][1] = True
    with suppress(Exception):
        if char_condition(input[line_index - 1][char_index + 1]):
            number = get_number_index(input[line_index - 1], line_index - 1, char_index + 1, numbers)
            if number:
                if not number_found[0][1]:
                    adjacent_number_indexes.append(number)
                number_found[0][2] = True

    # down
    with suppress(Exception):
        if char_condition(input[line_index + 1][char_index -1]):
            number = get_number_index(input[line_index + 1], line_index + 1, char_index -1, numbers)
            if number:
                adjacent_number_indexes.append(number)
                number_found[2][0] = True
    with suppress(Exception):
        if char_condition(input[line_index + 1][char_index]):
            number = get_number_index(input[line_index + 1], line_index + 1, char_index, numbers)
            if number:
                if not number_found[2][0]:
                    adjacent_number_indexes.append(number)
                number_found[2][1] = True
    with suppress(Exception):
        if char_condition(input[line_index + 1][char_index + 1]) and not number_found[2][1]:
            adjacent_number_indexes.append(
                get_number_index(input[line_index + 1], line_index + 1, char_index + 1, numbers))

    # left and right
    with suppress(Exception):
        if char_condition(input[line_index][char_index - 1]):
            adjacent_number_indexes.append(
                get_number_index(input[line_index], line_index, char_index - 1, numbers))
    with suppress(Exception):
        if char_condition(input[line_index][char_index + 1]):
            adjacent_number_indexes.append(
                get_number_index(input[line_index], line_index, char_index + 1, numbers))

    return adjacent_number_indexes

def get_gear_ratio(input, line_index, char_index, numbers):
    adjacent_numbers = get_gear_adjacent_number_indexes(input,
                                                        line_index,
                                                        char_index,
                                                        numbers)
    print(adjacent_numbers)
    if len(adjacent_numbers) == 2:
        return adjacent_numbers[0] * adjacent_numbers[1]
    return 0

def get_gear_ratios(input, numbers):
    gear_ratios = []
    for i, line in enumerate(input):
        for j, char in enumerate(line):
           if char == '*':
               gear_ratios.append(get_gear_ratio(input, i, j, numbers))
    return gear_ratios

def main():
    input = read_input()
    numbers = get_numbers_from_input(input)
    gear_ratios = get_gear_ratios(input, numbers)
    print(sum(gear_ratios))


if __name__ == '__main__':
    main()