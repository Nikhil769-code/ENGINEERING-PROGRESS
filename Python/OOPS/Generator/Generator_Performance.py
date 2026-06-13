import mem_profile
import random 
import time 

names = ['John','Kenny','George','Adam','Nikhil']
majors = ['Math','Chemistry','Physics','Social-Science']

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }
        yield person

t1 = time.clock()
people = people_list(100000)
t2 = time.clock()

t1 = time.clock()
people = people_generator(100000)
t2 = time.clock()

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_resource()))
print('Took {} Seconds'.format(t2-t1))
