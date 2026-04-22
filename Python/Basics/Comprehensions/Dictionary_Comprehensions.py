names = ['nick','nick2','nick3','nick4']
heroes = ['iron','bat','wolv','deadp']

print(list(zip(names , heroes)))
# zip():
# - Pairs elements from both lists → returns iterator of tuples
# - list() converts it into a readable list


# -------------------- Create Dictionary (Loop) --------------------

# Goal: {'name': 'hero'} mapping
my_dict = {}

for name, hero in zip(names, heroes):
    my_dict[name] = hero  
    # Assign each name → corresponding hero

print(my_dict)


# -------------------- Dictionary Comprehension --------------------

my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'nick'}
# Creates dictionary in one line
# Includes condition → excludes 'nick'

print(my_dict)