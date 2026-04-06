class Person:
    num_of_emps = 0
    raise_amount = 4.03
    def __init__(self,firstname,lastname,age,gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender 
        Person.num_of_emps +=1
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)
    def apply_raise(self):
        self.age = int(self.age * self.raise_amount)


p1 = Person("Amit","Kumar",21,"Male") #This is instance variable
p2 = Person("Prince","Gupta",21,"Bi")
print(p1.num_of_emps)

# print(p2.__dict__)
# print(Person.raise_amount)
# print(p1.raise_amount)
# print(p2.raise_amount)
'''so basically when i try to access num_of_emps through my instance variable p1 ,
 what it does is that it access the value of num_of_emps from class as it itself don't have that attribute .
   also , the value of num_of_emps = 0 changes to 2 because of the 2 instance variables defined'''