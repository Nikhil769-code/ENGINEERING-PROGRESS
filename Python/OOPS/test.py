class Person:
    raise_amount = 1.02
    def __init__(self, pay , name):
        self.pay = pay
        self.name = name

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    def appy_raise(self):
        self.pay = int(self.pay * 2.02)

p1 = Person(500,"Nikhil")
p2 = Person(1000,"Nick")
Person.set_raise_amount(1.06)
print(Person.raise_amount)
print(p1.raise_amount)
print(p2.raise_amount)



