class Bicycle(object):
    def __init__(self, model, weight, cost, stock):
        self.model = model
        self.weight = weight
        self.cost = cost
        self.stock = stock

class BikeShop(object):
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.margin = 20

    def sell_bike(self, bicycle):
        self.total_bike = self.margin + bicycle.cost

class Customer(object):
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        self.can_buy = True


def can_buy(inventory, customer):
    print(customer.name, "can afford:")

    for i in inventory:
        if i.cost < customer.funds:
            print(i.model)

def purchase_bike(bike, customer):
    print("{} purchased {} for ${}".format(customer.name, bike.model, bike.cost))
    leftover_funds = customer.funds - bike.cost
    print("They have ${} left".format(leftover_funds))
    bike.stock -= 1
    return bike.stock

def profit(inventory, old_total, bikes_sold):
    total = 0
    for bike in inventory:
        total_bike = bike.stock * bike.cost
        total += total_bike
    profit = old_total - (total + procycles.margin * bikes_sold)
    return profit

procycles = BikeShop("Pro Cycles", [])

bridgestone = Bicycle("Bridgestone Picnica", 46, 261, 3)
procycles.inventory.append(bridgestone)

honda = Bicycle("Honda RN-01 G-cross", 57, 316, 2)
procycles.inventory.append(honda)

lancia = Bicycle("Lancia Urban Bike", 47, 198, 5)
procycles.inventory.append(lancia)

lotus = Bicycle("Lotus 108", 39, 550, 3)
procycles.inventory.append(lotus)

miyata = Bicycle("Miyata 310", 50, 267, 1)
procycles.inventory.append(miyata)

panasonic = Bicycle("Panasonic Sport Deluxe", 40, 201, 5)
procycles.inventory.append(panasonic)

hailey = Customer("Hailey", 200)
linus = Customer("Linus", 500)
alice = Customer("Alice", 1000)

can_buy(procycles.inventory, hailey)
print("\n")
can_buy(procycles.inventory, linus)
print("\n")
can_buy(procycles.inventory, alice)

print("\n")
for bike in procycles.inventory:
    print("There are {} of {} in stock.".format(bike.stock, bike.model))

original_total = 0
for bike in procycles.inventory:
    bike_total = bike.stock * bike.cost
    original_total += bike_total

bikes_sold = 0
print("\n")
purchase_bike(lancia, hailey)
bikes_sold += 1
print("\n")
purchase_bike(honda, linus)
bikes_sold += 1
print("\n")
purchase_bike(lotus, alice)
bikes_sold += 1

print("\n")
for bike in procycles.inventory:
    print("There are {} of {} left in stock.".format(bike.stock, bike.model))

print("\n")
print("They made $", profit(procycles.inventory, original_total, bikes_sold), "profit.")
