class CoffeeMachine:
    def __init__(self):
        self.capacity = 5
        self.bill = 0


class CoffeeType:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price


coffees = []

coffee = CoffeeMachine()

def calculate(c):
    if c >= 1 and c <= len(coffees):
        q = int(input("Enter the quantity"))
        if(q*coffees[c-1].size > coffee.capacity*1000):
            print('Not enough coffee in the dispense')
            return
        
       
        coffee.bill = coffee.bill + (q * coffees[int(c)-1].price)
        coffee.capacity = ((coffee.capacity*1000) - (q*coffees[c-1].size))/1000 



coffees.append (CoffeeType('Normal Coffee', 120, 60))
coffees.append (CoffeeType('Filter Coffee', 200, 70))
coffees.append (CoffeeType('Normal Coffee', 180, 100))
coffees.append (CoffeeType('Normal Coffee', 220, 110))
coffees.append (CoffeeType('Normal Coffee', 250, 150))


while True:
    print("Welcome to the coffee machine!")
    c = int(input("Enter the choice"))
    calculate(c)
    choice = input("Do you want anything else, Y/N")
    if choice.lower() != 'y':
        break

print(f"{coffee.bill}")