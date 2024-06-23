import Bookstore
import sys
import time
import csv

store = Bookstore.Bookstore()

day = 1

dayFilePath = "day.txt"
with open(dayFilePath, "r") as dayFile:
    data = dayFile.read()
    day = int(data)

filename = "PythonProductInventory" + str(day) + ".csv"
with open(filename, "r") as CSVFile:
    reader = csv.reader(CSVFile)    

    fields = next(reader)
    for row in reader:
        if row[1] == "book":
            store.addBook(row[2], float(row[5]), int(row[4]), row[3])
        elif row[1] == "cd":
            store.addCD(row[2], float(row[5]), int(row[4]), row[3])
        elif row[1] == "dvd":
            store.addDVD(row[2], float(row[5]), int(row[4]))



def getIntInput(min:int=None, max:int=None, message="Enter your selection: "):
    while True:
        try:
            userSelection = int(input(message))
            if min == None or max == None:
                return userSelection
            elif userSelection >= min and userSelection <= max:
                return userSelection
            else:
                print("Selection must be between " + str(min) + " and " + str(max))
        except:
            print("Not a valid integer selection, try again")



while True:
    menu = """Welcome to Bookstore Menu. Day: """ + str(day) + """
    0. Exit Program
    1. Make a purchase
    2. Add an item to inventory
    3. Display inventory
    4. Reset to Day 1
Select an option: """

    menuChoice = getIntInput(0, 4, menu)

    match menuChoice:
        case 0:
            print("Store revenue for day " + str(day) + " is $" + str(store.dailyStoreRevenue))

            with open("C:/Stuff/pythonProjects/bookstoreProject/PythonProductInventory" + str(day + 1) + ".csv", "w") as f:
                f.write("productID,type,title,author/artist,numInStock,price\n")
                for x in store.inventoryList:
                    if x.type == "book":
                        f.write(str(x.IDNum) + "," + x.type + "," + x.title + "," + x.author + "," + str(x.quantity) + "," + str(x.price) + "\n")
                    elif x.type == "cd":
                        f.write(str(x.IDNum) + "," + x.type + "," + x.title + "," + x.artist + "," + str(x.quantity) + "," + str(x.price) + "\n")
                    elif x.type == "dvd":
                        f.write(str(x.IDNum) + "," + x.type + "," + x.title + ",n/a," + str(x.quantity) + "," + str(x.price) + "\n")

            with open(dayFilePath, "w") as dayFile2:
                dayFile2.write(str(day + 1))
                

            sys.exit(0)
        case 1:
            store.displayInventory()
            itemChoice = getIntInput(1, len(store.inventoryList), "Select the item to purchase: ")
            print("There are " + str(store.inventoryList[itemChoice-1].quantity) + " copies in stock")
            quantityChoice = getIntInput(0, int(store.inventoryList[itemChoice-1].quantity), "Enter desired quantity: ")
            total = store.makePurchase(itemChoice, quantityChoice)
            print("Customer total is $" + str(total))
            time.sleep(2)
        case 2:
            print("Item Types:\n    1. Book\n   2. CD\n    3. DVD")
            type = getIntInput(1, 2, "Enter type of new item: ")
            title = input("Enter title of item: ")
            price = input("Enter price of item: $")
            quantity = input("Enter quantity of item: ")

            if type == 1:
                author = input("Enter author of book: ")
                store.addBook(title, price, quantity, author)
            elif type == 2:
                artist = input("Enter artist of CD: ")
                store.addCD(title, price, quantity, artist)
            elif type == 3:
                store.addDVD(title, price, quantity)
        case 3:
            store.displayInventory()
        case 4:
            with open(dayFilePath, "w") as dayFile3:
                dayFile3.write("1")
            
            print("Store revenue for day " + str(day) + " is $" + str(store.dailyStoreRevenue))
            sys.exit(0)



    