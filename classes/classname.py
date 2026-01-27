class Dog:
    species = "French Bulldog"

    def __init__(self, name):
        self.name = name

print(Dog.species)

dog1 = Dog("Jack")

print(dog1.name)
print(dog1.species)

dog2 = Dog("Blue")
print(dog2.name)
print(dog2.species)



class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

car_1 = Car("grey", "Acura TLX")
car_2 = Car("black", "VW Bug")

print(car_1.model)
print(car_2.model)

print(car_1.color)
print(car_2.color)



class Employee:
    def __init__(self, name, id_num, role):
        self.id_num = id_num
        self.role = role
        self.name = name

    def task(self, id_num):
        return f"{self.name} does not have an ID#: {id_num}"

employee_1 = Employee(1, "Manager", "Jeff")
employee_2 = Employee(2, "Assistance to the...", "Bibby")

print(employee_1.id_num)
print(employee_1.role)

print(employee_2.id_num)
print(employee_2.role)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        return f"{self.name} says MEEOWWW"

cat_1 = Cat("Gerlad", 4)
cat_2 = Cat("Jak", 69)

print(cat_1.name)
print(cat_1.age)


print(cat_2.name)
print(cat_2.age)

cat_1 = Cat("Puss", 7)
cat_2 = Cat("Boots", 4)

print(cat_1.meow())
print(cat_2.meow())

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self)
        return f"'{self.title}' has {self.pages} pages."

    def __eq__(self, other):
        return self.pages == other.pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1)) # 420
print(len(book2)) # 420
print(str(book1)) # 'Built Wealth Like a Boss' has 420 pages
print(str(book2)) # 'Be Your Own Start' has 420 pages
print(book1 == book2) # True


print(str(book1))
