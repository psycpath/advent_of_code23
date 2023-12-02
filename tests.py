def is_possible(game_info, cube_counts):
    for subset in game_info:
        subset_counts = {color: 0 for color in cube_counts.keys()}
        for item in subset:
            color, count = item.split()
            subset_counts[color] += int(count)
        
        if any(subset_counts[color] > cube_counts[color] for color in cube_counts.keys()):
            return False
    
    return True

def possible_games(input_data, cube_counts):
    possible_ids = []
    for line in input_data:
        game_id, game_info = line.split(": ")
        game_info = [subset.split(", ") for subset in game_info.split("; ")]
        
        if is_possible(game_info, cube_counts):
            possible_ids.append(int(game_id.split()[1]))

    return possible_ids

# Replace the input_data variable with your actual puzzle input
input_data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

cube_counts = {'red': 12, 'green': 13, 'blue': 14}
result = sum(possible_games(input_data, cube_counts))
print(result)