print('\nOutput for challenge day 1 test\n')


with open('day_1/input.txt') as file:
    lines = file.readlines()


dict = {
    "one" : "o1e",
    "two" : "t2o",
    "three" : "t3e",
    "four" : "f4r",
    "five" : "f5e",
    "six" : "s6x",
    "seven" : "s7n",
    "eight" : "e8t",
    "nine" : "n9e"
    }

sum_of_all_numbers = 0
numbers = str()


for line in lines:
    line = line.strip()

    for key in dict:
        line = line.replace(key, str(dict[key]))
    for char in line:
        if char.isdigit():
            numbers += char
    sum_of_all_numbers += int(str(numbers[0]) + str(numbers[-1]))

    numbers = str()
    
print(sum_of_all_numbers)


#if on a line only one number appears, the callibration value the two digit consisting of twice that number?? unintuitive
