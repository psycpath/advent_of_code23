print('\nOutput for challenge day 1\n')


with open('day_1/input.txt') as file:
    lines = file.readlines()


dict = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
    }

sum_of_all_numbers = 0
numbers = str()
for line in lines:
    print(line)
    for key in dict:
        while key in line:
            line.replace(key, str(dict[key]))
            numbers += str(dict[key])
    print(line)
#   sum_of_all_numbers += int(str(numbers[0]) + str(numbers[len(numbers)-1]))
#   print(numbers)
#   numbers = str()


#print((sum_of_all_numbers))
            
