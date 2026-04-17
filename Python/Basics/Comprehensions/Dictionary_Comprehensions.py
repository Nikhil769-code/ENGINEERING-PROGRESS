names = ['nick','nick2','nick3','nick4']
heroes = ['iron','bat','wolv','deadp']
print(list(zip(names , heroes)))
  
#  I want a dict{'name' : 'hero'} for each name,hero in zip(names, heroes)
my_dict = {}
for name,hero in zip(names, heroes):
    my_dict[name] = hero 
print(my_dict)

#  DICTIONARY COMPREHENSION 

my_dict = {name: hero for name,hero in zip(names, heroes) if name != 'nick'}
print(my_dict)