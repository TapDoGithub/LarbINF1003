import json
import product

inventory = []
def load_inventory():

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
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    count = int(input("Enter product quantity: "))

    entry = entry_process(len(inventory), str(count), str(price), name)
    if entry != "failed":
        new_product =product.product(entry["itemName"], entry["price"], entry["count"])
        inventory.append(new_product)


def update_product():
    print("Updating a product")
    id = input('Product ID: ')
    search_result = select_product(id)
    if search_result != None:
        itemName = input('New Product Name: ')
        price = input('New Price: ')
        count = input('New Stock Quantity: ')

        updated_entry = entry_process(len(inventory), str(count), str(price), itemName)

        if updated_entry != "failed":
            inventory.remove(search_result)
            new_product = product.product(updated_entry["itemName"], updated_entry["price"], updated_entry["count"])
            inventory.append(new_product)
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

    for index, item in enumerate(inventory):
        if item == "failed":
            continue

        if isinstance(item, dict):
            product_id = item.get('id', index)
            name = item.get('itemName', '')
            price = item.get('price', '')
            count = item.get('count', '')
        else:
            product_id = getattr(item, 'id', index)
            name = getattr(item, 'itemName', '')
            price = getattr(item, 'price', '')
            count = getattr(item, 'count', '')

        print(f"ID:{product_id}|Name:{name}|Price:{price}|Stock:{count}")
    