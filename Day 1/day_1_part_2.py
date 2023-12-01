
digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven':7, 'eight': 8, 'nine': 9,
          '1': 1, '2': 2, '3': 3, '4': 4, '5':5, '6': 6, '7': 7, '8': 8, '9': 9}
sum = 0
f = open("day_1_input.txt", "r")
for line in f:
    digits_in_line = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6:-1, 7: -1, 8: -1, 9: -1}
    for digit in digits:
        position = line.find(digit)
        if position != -1:
            if digits_in_line[digits[digit]] == -1 or position < digits_in_line[digits[digit]]:
                digits_in_line[digits[digit]] = position
    min = 10000
    min_digit = 10
    for digits_in_line_key in digits_in_line:
        if digits_in_line[digits_in_line_key] != -1 and digits_in_line[digits_in_line_key] < min:
            min = digits_in_line[digits_in_line_key]
            min_digit = digits_in_line_key
    sum += min_digit * 10

    digits_in_line = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6:-1, 7: -1, 8: -1, 9: -1}
    for digit in digits:
        position = line.rfind(digit)
        if position != -1:
            if digits_in_line[digits[digit]] == -1 or position > digits_in_line[digits[digit]]:
                digits_in_line[digits[digit]] = position
    max = -1
    max_digit = 0
    for digits_in_line_key in digits_in_line:
        if digits_in_line[digits_in_line_key] != -1 and digits_in_line[digits_in_line_key] > max:
            max = digits_in_line[digits_in_line_key]
            max_digit = digits_in_line_key
    sum += max_digit
    line = line.replace('\n', '')
    print(f"{line} - {min_digit}{max_digit}")

print(sum)