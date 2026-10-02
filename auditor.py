import json

# Global Variables
inventory = []

# Inventory
def load_inventory():
    global inventory

    try:
        with open('inventory.json', 'r') as file:
            inventory = [json.loads(line) for line in file if line.strip()]
            
    except FileNotFoundError:
        inventory = []

def save_inventory():
    with open('inventory.json', 'w') as file:
        for item in inventory:
            if item != "failed":
                json.dump(item, file)
                file.write('\n')

# Entry
def select_product(id):
    for item in inventory:
        if item['id'] == id:
            return item
    return None

def entry_process(id=len(inventory), count=None, price=None, itemName=None):

    if count.isdigit() and int(count) > 0:
        return {"id": id, "itemName": itemName, "price": float(price), "count": int(count)}
    else:
        return "failed"

def add_product():
    print("Adding a new product")
    id = input('Product ID: ')
    itemName = input('Product Name: ')
    price = input('Product Price: ')
    count = input('Stock Quantity: ')
    new_entry = entry_process(id, count, price, itemName)
    inventory.append(new_entry)

def update_product():
    print("Updating a product")
    id = input('Product ID: ')
    search_result = select_product(id)
    if search_result != None:
        itemName = input('New Product Name: ')
        price = input('New Price: ')
        count = input('New Stock Quantity: ')

        updated_entry = entry_process(id, count, price, itemName)
        if updated_entry != "failed":
            inventory.remove(search_result)
            inventory.append(updated_entry)
            print(f"Product {id} updated successfully.")
        else:
            print("Invalid stock quantity. Update failed.")
    else:
        print("Product not found.")

def search_product():
    print ("Searching product")
    id = input('Enter product ID to search: ')
    item = select_product(id)
    if item != None:
        print(f"ID:{item['id']}|Name:{item['itemName']}|Price:{item['price']}|Stock:{item['count']}")
    else:
        print("Product not found.")

def display_all():
    print("Displaying all products:")

    for item in inventory:
        if item != "failed":
            print(f"ID:{item['id']}|Name:{item['itemName']}|Price:{item['price']}|Stock:{item['count']}")
    
# Report
def generate_report(i):
    units = sum(c["count"] for c in i if isinstance(c, dict))
    failed = i.count("failed")
    print(f'Total Process Units: {units}')
    print(f'Failed Entries: {failed}')
    print(f'Tax Total: {calculate_tax(units)}')

# Calculation
def process_delivery(current_total, new_entry):
    return current_total + new_entry["count"] if new_entry != "failed" else current_total


def calculate_tax(total_units):
    tax_rate = 0.1
    return total_units * tax_rate

# Main
def main():
    global inventory
    total_units = 0

    load_inventory()
    while True:
        print("MENU")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Search Product")
        print("5. Save inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")
        print("\n")
        if choice == "1":
            display_all()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_product()
        elif choice == "4":
            search_product()
        elif choice == "5":
            save_inventory()
        elif choice == "6":
            print("Saving inventory and exiting...")
            save_inventory()
            break

if __name__ == "__main__":
    main()