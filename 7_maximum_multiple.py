divisor = int(input())
bound = int(input())

result = 0
for number in range(1, bound + 1):
    if number % divisor == 0:

        result = number
print(result)