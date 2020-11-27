"""Supermarket checkout class used for learning pytest"""

class Checkout:

    class Discount:
        def __init__(self, nItems, price):
            self.nItems = nItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
        self.total = 0

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total

    def calculateItemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.nItems:
                total += self.calculateItemDiscount(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def calculateItemDiscount(self, item, cnt, discount):
        total = 0
        nOfDiscounts = cnt / discount.nItems
        total += nOfDiscounts * discount.price
        remaining = cnt % discount.nItems
        total += remaining * self.prices[item]
        return total


    def addDiscount(self, item, nOfItems, price):
        discount = self.Discount(nOfItems, price)
        self.discounts[item] = discount