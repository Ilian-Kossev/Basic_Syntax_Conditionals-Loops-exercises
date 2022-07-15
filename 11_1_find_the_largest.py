number = int(input())
number_to_string = str(number)
result = ''
value = 10
for index in range(len(number_to_string)):
    digit = int(number_to_string[index])

    for index2 in range(len(number_to_string)):
        digit_1 = int(number_to_string[index2])
        if value >= digit:
            continue
        if digit >= digit_1:
            value = digit
        else:
            value = digit_1
    value_to_string = str(value)
    result += value_to_string

print(result)
547284
547284



