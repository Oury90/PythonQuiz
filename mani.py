# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.forward(100)
#
# timmy_screen = Screen()
# timmy_screen.exitonclick()


# list in python
# items_list = ["Orange", "Banane", "Mangue", "Avocat"]
#
# items_list[3] = "Avocats"
#
# items_list.append("Clementine")
#
# items_list.append(["item1", "item2"])
# print(items_list)
# items_list.pop(5)
# print(items_list)

# import random
# jokes = ["Head", "Tail"]
#
# choice_number = random.randint(0,1)
# user_choice = int(input("Choice your number"))
#
# if choice_number == 0 and user_choice == 1:
#     print("You vin")
# elif choice_number == 1 and user_choice ==0:
#     print("You lose")
# else:
#     print("Is egal")

# class Dog:
#     species = "Canine"  # Class attribute
#
#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute
#
# # Creating an object of the Dog class
# dog1 = Dog("Buddy", 3)
#
# print(dog1.name)
# print(dog1.species)

# class Person:
#       def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#       def greating(self, name):
#           heatin = f"Hello {self.name}"
#           print(heatin)
#
#
# p1 = Person("John", 36)
# p2 = Person("Amadou", "12")
#
# # print(p1.age)
# print(p1.greating(oury))

from oury import Person

pizza = Person("S", 0)
if pizza.size == "S":
    pizza.bill = 12
elif pizza.size == "M":
    pizza.bill = 15
elif pizza.size == "L":
    pizza.bill = 20


if pizza.addCheese() == "Y":
    if pizza.size == "S":
        pizza.bill +=2
    else:
        pizza.bill += 3

if pizza.addCheese() == 'Y':
    pizza.bill +=1


print(f"Your final bill is: {pizza.bill}")