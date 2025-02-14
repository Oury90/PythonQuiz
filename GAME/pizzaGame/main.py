
bill = 0
print("Welcome to my game pizza")
# Make choice size for you Pizza
size = input("What size would you like? S, M, L ")
if size == "S" or size == "M" or size == "L":
    if size == "S":
        bill = 12
    elif size == "M":
        bill = 15
    elif size == "L":
        bill = 17

    # Ask the customer if they would like add peperoni
    peperoni = input("Would you like to add peperoni Y or N ")
    if peperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill +=3

    # Ask the customer if the would like to add cheeses
    cheeses = input("Would you like to add cheeses Y or N ")
    if cheeses == "Y":
        bill += 1

    print(f"The final bill is {bill}")
else:
    print("Please Enter the valid Size.")