print('\nOutput for challenge day 1\n')


with open('day_1/input.txt') as file:
    lines = file.readlines()


numbers = str()
for line in lines:
    for char in line:
        if char.isdigit():
            print(char)
            
