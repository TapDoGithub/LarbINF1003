inventory=[]

def entry_process(I):

    if not I=="quit":
        if I.isdigit() and int(I)>0:
            return int(I)
        else:
            return "failed"
    else:
        generate_report(inventory)
        exit()

def process_delivery(current_total, new_entry):
    return current_total + new_entry if new_entry != "failed" else current_total

def generate_report(i):
    units = sum(c for c in i if isinstance(c, int))
    failed = i.count("failed")
    print(f'Total Process Units: {units}')
    print(f'Failed Entries: {failed}')
    print(f'Tax Total: {calculate_tax(units)}')

def calculate_tax(total_units):
    tax_rate = 0.1
    return total_units * tax_rate

def main():
    global inventory
    total_units = 0

    while True:
        new_entry = entry_process(input('enter stock quantity '))
        inventory.append(new_entry)

        total_units = process_delivery(total_units, new_entry)
        if total_units > 500:
            print("ALERT: total inventory exceeds 500 units")
            generate_report(inventory)
            break

main()