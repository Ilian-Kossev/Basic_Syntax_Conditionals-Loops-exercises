current_year = int(input())
while True:
    current_year += 1
    current_year_as_string = str(current_year)
    repetition_found = False
    for index in range(len(current_year_as_string) - 1):
        for index2 in range(index + 1, len(current_year_as_string)):
            if current_year_as_string[index] == current_year_as_string[index2]:
                repetition_found = True
                break
        if repetition_found:
            break
    if repetition_found:
        continue
    else:
        print(current_year)
        break
