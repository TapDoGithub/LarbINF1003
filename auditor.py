inventory=[]

def report():
    global inventory
    units = sum(c for c in inventory if isinstance(c, int))
    print('Total Process Units:', units)
    print('Failed Entries:', inventory.count('failed'))


def entry():
    global inventory

    I=input('enter stock quantity ')

    if not I=="quit":
        if I.isdigit() and int(I)>0:
            return int(I)
        else:
            return "failed"
    else:
        report()
        exit()


def main():
    global inventory
    
    while True:
        inventory.append(entry())
        
        total_units = sum(c for c in inventory if isinstance(c, int))
        if total_units > 500:
            print("ALERT: total inventory exceeds 500 units")
            report()
            break

main()