# Global Variables
inventory = []

# Inventory
def load_inventory():
    global inventory

    
    try:
        with open('inventory.txt', 'r') as file:
            inventory = [line.strip() for line in file if line.strip()]
            print(f"Inventory: \n {chr(10).join(inventory)}")
    except FileNotFoundError:
        inventory = []

def save_inventory():
    with open('inventory.txt', 'w') as file:
        for item in inventory:
            if item != "failed":
                file.write(f"{item}\n") 

# Entry
def entry_process(count,itemName):

    if not count or itemName == "quit":
        if count.isdigit() and int(count) > 0:
            return {"id": len(inventory), "itemName": itemName, "count": int(count)}
        else:
            return "failed"
    else:
        generate_report(inventory)
        save_inventory()
        exit()

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
        itemName = input('enter item name: ')
        count = input('enter stock quantity: ')
        new_entry = entry_process(count, itemName)
        inventory.append(new_entry)

        total_units = process_delivery(total_units, new_entry)
        if total_units > 500:
            print("ALERT: total inventory exceeds 500 units")
            save_inventory()
            generate_report(inventory)
            break

main()