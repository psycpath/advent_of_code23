print('\nOutput for challenge day 3\n')

with open('day_3/input.txt') as file:
    lines = file.readlines()

print(lines[0])
index = 0
x = 0
sum_of_part_numbers = 0

for line in lines:
    
    if index == 0:
        for item in line:
            if item.isdigit():
                if not line[x+1].isdigit:
                    len_part = 1
                    
                if not "." in "." in lines[index -1][x-1:x+3] or not "." in lines[index][x-1] or not "." in lines[index][x + 3]:
                    sum_of_part_numbers += int(str(line[x]) + str(line[x+1]) + str(line[x + 2]))
            x += 1

    if index == len(lines)-1:
        for item in line:
            if item.isdigit():
                if not "." in "." in lines[index + 1][x-1:x+3] or not "." in lines[index][x-1] or not "." in lines[index][x + 3]:
                    sum_of_part_numbers += int(line[x] + line[x+1] + line[x + 2])
                
    for item in line:
        if item.isdigit():
            if not "." in lines[index - 1][x-1:x+3] or not "." in "." in lines[index + 1][x-1:x+3] or not "." in lines[index][x-1] or not "." in lines[index][x + 3]:
                sum_of_part_numbers += int(line[x] + line[x+1] + line[x + 2])
                
        x += 1
    index += 1
    
print(sum_of_part_numbers)

            