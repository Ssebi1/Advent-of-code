sum = 0
f = open("day_1_input.txt", "r")
for line in f:
    for char in line:
        if char > '0' and char <= '9':
            sum += int(char) * 10
            break
    for char in line[::-1]:
        if char > '0' and char <= '9':
            sum += int(char)
            break

print(sum)