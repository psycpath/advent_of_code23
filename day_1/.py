print('\nOutput for challenge day 1\n')


with open('day_1/input.txt') as file:
    lines = file.readlines()

sum_of_all_numbers = 0
numbers = str()
for line in lines:
    for char in line:
        if char.isdigit():
            numbers += char
    sum_of_all_numbers += int(str(numbers[0]) + str(numbers[len(numbers)-1]))
    numbers = str()

print((sum_of_all_numbers))
            
