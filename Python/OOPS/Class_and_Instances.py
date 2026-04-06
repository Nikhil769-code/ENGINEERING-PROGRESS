class Person:
    def __init__(self,firstname,lastname,age,gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender 
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)
    



p1 = Person("Amit","Kumar",21,"Male") #This is instance variable
p2 = Person("Prince","Gupta",21,"Bi")
print(p1.fullname())
print(p2.fullname())
print(Person.fullname(p1))