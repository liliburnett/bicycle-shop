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
