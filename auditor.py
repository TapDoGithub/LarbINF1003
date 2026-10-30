
import product 
import inventory_manager

inventory = inventory_manager.inventory


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
    inventory_manager.load_inventory()
    total_units = 0

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
        options = {"1": inventory_manager.display_all, "2": inventory_manager.add_product, "3": inventory_manager.update_product, "4": inventory_manager.search_product, "5": inventory_manager.save_inventory, "6": exit}
        if choice in options:
            options[choice]()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()