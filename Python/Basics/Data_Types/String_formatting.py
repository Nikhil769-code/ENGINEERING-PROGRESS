person = {'name':'Jennifer','age':22}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old . '
# Basic string concatenation (manual + needs type conversion)
print(sentence)


sentence1 = 'My name is {} and I am {} years old .'.format(person['name'],person['age'])
# Using {} placeholders with .format()
print(sentence1)


sentence1 = 'My name is {0} and I am {1} years old .'.format(person['name'],person['age'])
# Positional indexing inside format()
print(sentence1)


tag = 'hl'
text = 'This is a headline'
sentence2 = '<{0}>{1}</{0}>'.format(tag,text)
# Reusing same argument using index
print(sentence2)


sentence3 = 'My name is {0[name]} and I am {1[age]} years old .'.format(person,person)
# Accessing dictionary keys inside format()
print(sentence3)

sentence4 = 'My name is {0[name]} and I am {0[age]} years old .'.format(person)
# Using same object multiple times
print(sentence4)


li = ['Jenny',23]
sentence5 = 'My name is {0[0]} and I am {0[1]} years old.'.format(li)
# Accessing list elements inside format()
print(sentence5)


class Person():
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    

p1 = Person('Jackson',25)

sentence6 = 'My name is {0.name} and I am {0.age} years old '.format(p1)
# Accessing object attributes inside format()
print(sentence6)


sentence7 = 'My name is {name} and I am {age} years old '.format(name='Jenn',age=30)
# Using keyword arguments in format()
print(sentence7)


sentence8 = 'My name is {name} and I am {age} years old . '.format(**person)
# Unpacking dictionary (**dict) → most readable approach
print(sentence8)


for i in range(1,11):
    sentence9 = 'The value is {:03}'.format(i)
    # Zero padding → ensures 3 digits (e.g., 001, 002)
    print(sentence9)


pi = 3.14159265
sentence10 = 'Pi is equal to {:.2f}'.format(pi)
# Float formatting → 2 decimal places
print(sentence10)


sentence11 = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
# Comma separator + decimal formatting
print(sentence11)


sentence12 = '1 MB is equal to {:,} bytes'.format(1000**2)
# Comma separator without decimals
print(sentence12)


import datetime 
my_date = datetime.datetime(2026,9,24,12,30,45)
# Creating datetime object
print(my_date)


sentence13 = '{:%B %d, %Y}'.format(my_date)
# Date formatting → Month Day, Year
print(sentence13)


sentence14 = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
# Multiple date formats:
# %A → weekday, %j → day of year
print(sentence14)