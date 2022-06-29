class Item:
    pay_rate=0.8 # Class Level attribute:    for discount 20%
    all=[]
    #constructor
    def __init__(self, name: str, price: float, quantity: 0):
        # Limiting the input
        assert price>=0, f"Given price {price} should be more than 0"
        assert quantity>=0, "Please Enter a positive quantity"

        #Assign to self object

        self.name=name
        self.price=price
        self.quantity=quantity
        #Action to execute
        Item.all.append(self)

    def calculatePrice(self):
        return self.price * self.quantity

    def applyDiscount(self):
        self.price= self.price * self.pay_rate



# item1=Item('Laptop', 1000, 1)
# item2=Item('Mobile', 200, 1)
#
# item1.applyDiscount()
# print(item1.price)
# item2.applyDiscount()
# print(item2.price)

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
for instance in Item.all:
    print(instance.name)