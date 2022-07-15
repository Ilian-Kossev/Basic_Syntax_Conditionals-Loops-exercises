word = input()

index = 0
for index in range(len(word)):
    letter = word[index]
    letter_to_number = ord(letter)
    if 65 <= letter_to_number <= 90:

        print(index, end=' ')


