"""
        Program: Warehouse management system
        Author: Wes Ray
    Description:  Description:
        1 - Register new item
            id (auto generated)
            title (str)
            category (str)
            stock (int)
            price (float)
        2 - Display Catalog
        3 - Update Stock
        4 - Remove item from catalog
        5 - Print Total stock value
        6 - Report - out of stock
"""
# imports
from menu import clear, print_menu, print_header, print_item
from item import Item
import pickle

# global variables
catalog = []
data_file = 'warehouse.data'

def serialize_catalog():
    global data_file
    writer = open(data_file, 'wb') # create/open a file to Write Binary
    pickle.dump(catalog, writer)
    writer.close() # close stream, release the file
    print("** Data serialized!")

def deserialize_catalog():
    try:
        global data_file
        reader = open(data_file, 'rb') # open file to read binary
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        print("** Deserialized " + str(len(catalog)) + " items")
    
    except:
        print("Error, could not load data")

#fn

def register_item():
    try:
        print_header("Register New Item")
        title = input('Please provide the Title: ')
        cat = input('Please provide the Category: ')
        price = float(input('Please provide the Price: '))
        stock = int(input('Please provide the Stock: '))

        id = 1
        item = Item(id, title, cat, price, stock)
        catalog.append(item)

        how_many = len(catalog)
        print("You now have: " + str(how_many) + " items on the catalog")

    except ValueError:
        print("Error: Incorrect value, try again")
    except: 
        print("Error, Somthing went wrong")
    
def print_catalog():
    print_header("Your Current Catalog")
    # travel the list
    # # print the title
    for item in catalog:
        print_item(item)
        
    
def print_no_stock():
    print_header("Items currently out of stock")
    for item in catalog:
        if (item.stock == 0):
            print_item(item)

def total_stock_value():
    
    total = 0.0
    for item in catalog:
        total += item.price * item.stock

    print("Total value: " + str(total))

def list_of_categories():
    result = []
    num = 0
    print_header("List of Catagories")
    for item in catalog:
        if item.category not in result:
            result.append(item.category)
    for item in result:
        num += 1
        print(" Category "+ str(num) + item.rjust(30)) 

def delete_item():
    item = choose_item("Please choose item to delete: ")
    if(item ! = 0):
        catalog.remove(item)
        print("**Item Has been Removed!!")

def update_stock():
    item = choose_item()
    if(item != 0):
        stock = int(input("Provide new stock value: "))
        item.stock = stock
        print("stock updated!!")

def choose_item(message):
    try:
        print_catalog()
        id = int(input("Please choose the ID to delete: "))
        found = False
        for item in catalog:
            if(item.id == id):
                found = True
                return item
        if(not found):
            print("**Error, invalid ID, verify and try again")
            return 0
    except:
        print("**Error, verify and try again")
        return 0
   
deserialize_catalog()


opc = ''
while(opc != 'x'):
    clear()
    print_menu()

    opc = input("Please choose an option: ")

    # if comparisons
    if(opc == '1'):
        register_item()
        serialize_catalog()
    elif(opc == '2'):
        print_catalog()
    elif(opc == '3'):
        print_no_stock() 
    elif(opc == '4'):
        delete_item()
        
    elif(opc == '5'):
        update_stock()
    elif(opc == '7'):
        total_stock_value()
    elif(opc == '8'):
        list_of_categories()
        
    
    

    else:
        print("Please choose a valid option")
    
    input("Press Enter to continue...")
    clear()

print('Good Bye!!')