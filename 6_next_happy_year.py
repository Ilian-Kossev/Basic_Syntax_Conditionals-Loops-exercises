# judge dava 80% - raboti samo s 4 cifreno chislo!
year = input()

value_1 = int(year[0])
value_2 = int(year[1])
value_3 = int(year[2])
value_4 = int(year[3])
magic_number_found = False

for x in range(10):
    if value_1 == 0:
        value_1 = 1
    for number_1 in range(value_1, 11):
        if number_1 == 10:
            value_1 = 1
            break
        for number_2 in range(value_2, 11):
            if number_2 == 10:
                value_2 = 0
                break
            for number_3 in range(value_3, 11):
                if number_3 == 10:
                    value_3 = 0
                    break
                for number_4 in range(value_4 + 1, 11):
                    if number_4 == 10:
                        value_4 = 0
                        break
                    if not number_4 == number_3 and not number_4 == number_2 and not number_4 == number_1:
                        if not number_3 == number_2 and not number_3 == number_1:
                            if not number_2 == number_1:
                                magic_number_found = True
                                print(f"{number_1}{number_2}{number_3}{number_4}")
                                break
                if magic_number_found:
                    break
            if magic_number_found:
                break
        if magic_number_found:
            break
    if magic_number_found:
        break
