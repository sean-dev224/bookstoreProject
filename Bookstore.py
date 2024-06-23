import Item

class Bookstore:

    def __init__(self):
        self.inventoryList = []
        self.dailyStoreRevenue = 0

    def makePurchase(self, itemChoice, quantityChoice):
        for x in self.inventoryList:
            if x.IDNum == itemChoice:
                x.quantity -= quantityChoice
                total = quantityChoice * x.price
                self.dailyStoreRevenue += total
                return total


    def displayInventory(self):
        print("\n")
        for x in self.inventoryList:
            x.printInfo()
            print("-----")

    def addBook(self, title, price, quantity:int, author):
        a = Item.Book(title, price, quantity, author)
        self.inventoryList.append(a)

    def addCD(self, title, price, quantity:int, artist):
        a = Item.CD(title, price, quantity, artist)
        self.inventoryList.append(a)

    def addDVD(self, title, price, quantity:int):
        a = Item.DVD(title, price, quantity)
        self.inventoryList.append(a)
