print('\nOutput for challenge day 2\n')


with open('day_2/input.txt') as file:
    lines = file.readlines()

# As you continue your walk, the Elf poses a second question: in each game you played,
# what is the fewest number of cubes of each color that could have been in the bag to 
# make the game possible?
#
sum_of_powers = 0
    
for line in lines:

    redmin = 0
    greenmin = 0
    bluemin = 0
    
    line = line.strip("\n")
    games =  line.split(": ")[1].split("; ")
    
    
    for game in games:
        
        round = game.split(", ")
        for cube in round:
            
            if cube[-1] == "d" and int(cube.split()[0]) > redmin:
                redmin = int(cube.split()[0])
            elif cube[-1] == "n" and int(cube.split()[0]) > greenmin:
                greenmin = int(cube.split()[0])
            elif cube[-1] == "e" and int(cube.split()[0]) > bluemin:
                bluemin = int(cube.split()[0])
    sum_of_powers += (redmin * bluemin * greenmin)
    
print(sum_of_powers)

#2143       too low
#2737511487 too high
#94460487   too high
#83707 thats it kid