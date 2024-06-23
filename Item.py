class Item:

    static_ID = 1
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

        self.IDNum = Item.static_ID
        Item.static_ID += 1

    def printInfo(self):
        print("Title: " + self.title)
        print("Price: " + str(self.price))
        print("Quantity: " + str(self.quantity))



class Book(Item):
    def __init__(self, title, price, quantity, author):
        super().__init__(title, price, quantity)
        self.author = author
        self.type = "book"


    def printInfo(self):
        print("Item " + str(self.IDNum) + " - Book")
        super().printInfo()
        print("Author: " + str(self.author))

class CD(Item):
    def __init__(self, title, price, quantity, artist):
        super().__init__(title, price, quantity)
        self.artist = artist
        self.type = "cd"

    def printInfo(self):
        print("Item " + str(self.IDNum) + " - CD")
        super().printInfo()
        print("Artist: " + str(self.artist))


class DVD(Item):
    def __init__(self, title, price, quantity):
        super().__init__(title, price, quantity)
        self.type = "dvd"
    
    def printInfo(self):
        print("Item " + str(self.IDNum) + " - DVD")
        super().printInfo()

    