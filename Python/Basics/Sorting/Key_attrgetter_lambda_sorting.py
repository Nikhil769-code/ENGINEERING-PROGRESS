
li = [9,5,6,2,8,1,3]

s_li = sorted(li , reverse=True)  
# sorted() function:
# - Returns a new sorted list (does NOT modify original)
# - Works with any iterable (list, tuple, dict, etc.)
# - Always returns a list
print('Sorted Variable :\t' , s_li)

li.sort(reverse=True)   
# sort() method:
# - Sorts the list in-place (modifies original list)
# - Returns None
# - Works only on lists
print('Original Variable :\t' , li)


tup = (9,7,5,3,6,2,1)
s_tup = sorted(tup)  
# sorted() converts tuple → list and sorts it
print('Tuple\t',s_tup)


di = {'name':'Nick','job':'Backend Engineer','age':'None','os':'Windows'}
s_di = sorted(di)  
# For dictionaries:
# - sorted() returns a list of keys (sorted alphabetically)
print('Dictionary\t',s_di)


li1 = [-6,-5,-4,1,2,3]
s_li1 = sorted(li1,key=abs)  
# key parameter:
# - Used to customize sorting logic
# - Here, sorting is based on absolute values
print (s_li1)


from operator import attrgetter  
# attrgetter:
# - Works similar to lambda for attribute access
# - Extracts attributes from objects (like .name, .age, etc.)
# - Faster and cleaner than lambda in simple cases


class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age 
        self.salary = salary
    
    def __repr__(self):  
        # __repr__:
        # - Defines how the object is displayed when printed
        return f'{self.name},{self.age},{self.salary}'


e1 = Employee('Nikhil',21,100000)
e2 = Employee('Vivek',23,30000)
e3 = Employee('Prince',22,20000)

employees = [e1,e2,e3]


# def e_sort(emp):
#     return emp.name


# s_employees = sorted(employees,key=e_sort) 

s_employees = sorted(employees,key=lambda emp : emp.name)  
# lambda:
# - Anonymous (unnamed) function
# - Takes emp → returns emp.name
# - Used as key for sorting

s_employees = sorted(employees,key=attrgetter('age'))  
# attrgetter:
# - Extracts 'age' attribute from each object
# - Used as key for sorting


'''
Internal working of sorted() with key:

for emp in employees:
    key_value = e_sort(emp)

- Python calls the key function on each object
- Uses returned values as comparison keys
- Sorts original objects based on those values
'''

print(s_employees)
