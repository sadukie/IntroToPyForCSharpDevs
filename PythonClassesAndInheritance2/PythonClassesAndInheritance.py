
from Person import Person
from Employee import Employee

p = Person("Thomas")
print(p)
print(isinstance(p,Person))

e = Employee("Bart","Senior Software Engineer")
print(e)

# Inheritance check
print("Is Bart an employee?")
print(isinstance(e,Employee))
print("Is Bart a person?")
print(isinstance(e,Person))

print("Is Thomas an employee?")
print(isinstance(p,Employee))

# Class level check
print(f'There are {p.getCount()} people according to {p.name}.')
print(f'There are {e.getCount()} people according to {e.name}.')