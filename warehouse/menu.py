import os

def print_menu():
    print("-" * 30)
    print(" Warehouse mgn sys")
    print("-" * 30)

    print("[1] Register New Item")
    print("[2] Display Catalog")
    print("[3] Items out of stock items")
    print("[4] Remove item from catalog")
    print("[5] Update Item Stock")
    print("[6] Update Item price")
    print("[7] Print Stock Value") # sum of all items (price * stock)
    print("[8] List of categories") # different cats (do not duplicate)

    print("[x] Close")

def print_header(title):
    clear()
    print("-" * 80)
    print(title)
    print("-" * 80) 

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

def print_item(item):
    print(    
        str(item.id).rjust(3)
        + " | " + item.title.ljust(25) 
        + " | " + item.category.ljust(12) 
        + " | " + str(item.stock).rjust(11)
        + " | $" + str(item.price).rjust(15)
    )
    print('-' * 80)