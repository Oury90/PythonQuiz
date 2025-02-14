class Person:
  def __init__(self, size, bill):
    self.size = size
    self.bill = bill
  def myChoice(self):
    size = input("What size do you need S, L, M").upper()
    # if size == "S":
    #   self.bill = 12
    # elif size == "M":
    #   self.bill = 15
    # else:
    #   self.bill = 20

  def choicePepp(self):
    choice_peperony = input("Would you like add pepperony Y or N")
    #if choice_peperony == "Y":
      # if self.size == "S":
      #   self.bill += 2
      # else:
      #   self.bill += 3

  def addCheese(self):
    add_cheese = input("Would you like add cheese Y or N")
    # if add_cheese == "Y":
      # self.bill += 1
    # print(f"Your final bill is: {self.bill}")