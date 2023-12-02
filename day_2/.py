print('\nOutput for challenge day 2\n')


with open('day_2/input.txt') as file:
    lines = file.readlines()

# Determine which games would have been possible if the bag had been
# loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?
    
    sum_of_ID = 0
    
for line in lines:
    z = 0
    round
    
    line = line.strip("\n")
    ID = int(line.split(": ")[0].split()[1])
    line = line.split(": ")[1]
    games = line.split("; ")
    
    #cube = 
    
    for game in games:
        round = game.split(", ")
        for cube in round:
            if cube[-1] == "d" and int(cube.split()[0]) > 12:
                z += 1
            elif cube[-1] == "n" and int(cube.split()[0]) > 13:
                z += 1
            elif cube[-1] == "e" and int(cube.split()[0]) > 14:
                z += 1
    if z == 0: 
        sum_of_ID += ID
print(sum_of_ID)

#3225: too High
