import csv
from random import randint
from typing import Optional

# function return removes event, otherwise returns None
def remove_event(id_to_remove: int, automatic: bool = False) -> Optional[dict]:
    
    check = confirmation()
    if not check:
        return None
        

    # the event is removed
    with open('events.csv', mode = 'r') as infile:
        csv_reader = csv.DictReader(infile)
        rows_n = [row for row in csv_reader] 
        rows = [row for row in rows_n if int(row['ID']) != id_to_remove]
        removed_row = [row for row in rows_n if int(row['ID']) == id_to_remove]

        # if specified event does not exist, program returns None
        if removed_row == []:
            if not automatic:
                print("Event with the specified ID does not exist")
            return 0

        # removing event
        with open('events.csv', mode = 'w', newline = '') as outfile:
            try:
                fieldnames = rows_n[0].keys()
            except:
                pass

            csv_writer = csv.DictWriter(outfile, fieldnames = fieldnames)
            
            csv_writer.writeheader()

            csv_writer.writerows(rows)
        
        
        if not automatic:
            print("Event successfully delated")

        return removed_row[0]
        

# to do sth, user have to confirm it by rewriting code e.g. '111', code to rewriting is generate automatically
# return True, when entered password is correct, otherwise return False
def confirmation() -> bool:
    qr: str = ''
    for _ in range(3):
        qr += str(randint(0, 9))

    print(f"Enter the code to confirm: {qr}")
    pw: str = input()

    if qr != pw.strip():
        print("The code is wrong. The Event has not been delated.")
        return False
    return True
        


# function changes the state of task; returns current state of event 
def done_undone(id_to_change):
    with open('events.csv', mode = 'r') as infile:
        csv_reader = csv.DictReader(infile)
        rows = [row for row in csv_reader] 

        # if specified event does not exist, program returns 0
        if rows == []:
            return 0

        rows[id_to_change-1]['State'] = '0' if rows[id_to_change-1]['State'] == '1' else '1'
        # filling csv
        with open('events.csv', mode = 'w', newline = '') as outfile:
            try:
                fieldnames = rows[0].keys()
            except:
                pass

            csv_writer = csv.DictWriter(outfile, fieldnames = fieldnames)
            
            csv_writer.writeheader()

            csv_writer.writerows(rows)

    return rows[id_to_change-1]['State']

def data_to_class(data):
    print(data)
    tab = [data['ID'], data['Type'], data['Name'], data['Date'], data['Description']]
    return tab

#operation what user wants to change, date, name etc
# def edit_event(id_to_edit, operation, new_data):
#     row_to_edit = remove_event(8)
#     if row_to_edit == 0:
#         print("This index doesn't exist")
#         return 0
#     tab = data_to_class(row_to_edit)
    # event = Event('Task', 'raport', 2024, 3, 1, 1, 1, 'aaaaa')



# tab = remove_event(8)
# print(tab)
if __name__ == "__main__":
    done_undone(1)