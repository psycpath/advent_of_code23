print('\nOutput for challenge day 3\n')

with open('day_3/input.txt') as file:
    lines = file.readlines()
    
index = 0

x = 0
sum_of_part_numbers = 0

for line in lines:
    line = line.strip("\n")

    for item in line:
        y = str()
        
        if item.isdigit():
            
            if line[x-1].isdigit():
                continue
            if not line[x+1].isdigit():
                len_part = 1
            elif line[x+1].isdigit() and not line[x+2].isdigit():
                len_part = 2
            else:
                len_part = 3

            if index == 0:
                try:
                    if not "." in lines[index + 1][x-1:(x+len_part)] or not "." in lines[index][x-1] or not "." in lines[index][x + (x+len_part)]:
                        for i in range(len_part):
                            print(line[x + (len_part)])
                        sum_of_part_numbers += int(y)
                
                except IndexError:
                    print("ignoring out of range error")

            elif index == len(lines)-1:
                if not "." in lines[index - 1][x-1:(x+len_part)] or not "." in lines[index][x-1] or not "." in lines[index][x + len_part]:
                    for i in range(len_part):
                        y += line[x + (len_part)]
                    sum_of_part_numbers += int(y)

            elif not "." in lines[index - 1][x-1:(x+len_part)] or not "." in lines[index + 1][x-1:(x+len_part)] or not "." in lines[index][x-1] or not "." in lines[index][x + len_part]:
                for i in range(len_part):
                    y += line[x + (len_part)]
                    sum_of_part_numbers += int

                    
                    
        x += 1
        
    index += 1
    x = 0
    
print(sum_of_part_numbers)

            