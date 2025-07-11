# Q no. 8:
# Write a program to input two sets of student roll numbers: one who play cricket and another who play football. 
# Find:
# a. Students who play both sports
# b. Students who play only one sport
# c. Students who play neither (given a master list of all students)

def analyze_sports_players(master_list, cricket_players, football_players):
    master_set = set(master_list)
    cricket_set = set(cricket_players)
    football_set = set(football_players)
    
    both_sports = cricket_set & football_set
    only_one_sport = cricket_set ^ football_set
    neither_sport = master_set - (cricket_set | football_set)
    
    return both_sports, only_one_sport, neither_sport

master_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cricket_players = [1, 2, 3, 5, 7]
football_players = [3, 4, 5, 6, 8]

both, only_one, neither = analyze_sports_players(master_list, cricket_players, football_players)

print("Students who play both sports:", both)
print("Students who play only one sport:", only_one)
print("Students who play neither sport:", neither)