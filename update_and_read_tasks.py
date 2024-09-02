import csv
from datetime import datetime
from typing import Optional
from random import randint

#get data from csv file
#returns None if data not exists, otherwise returns parsing* data
def read_and_parse_data(file_name: str, parse = True) -> Optional[list[dict]]:
    with open (file_name, mode = 'r') as file:
        csv_reader: csv.DictReader = csv.DictReader(file)
        data: list[dict] = [row for row in csv_reader]

    # return 0 if data does not exist
    if data == []:
         return None
    
    #data parsing
    if parse:
        for row in data:
            row['Date'] = datetime.strptime(row['Date'], "%Y-%m-%d %H:%M:%S")
            row['ID'] = int(row['ID'])

    return data
        
# sort data by their date and add indexes, 1 - the earliest one etc. 
# always returns data
#CHANGE NEEDED
def sort_and_add_index(data: Optional[list[dict]]) -> Optional[list[dict]]:
    #checks if data exists
    if data == None:
        return None
    # sort data by date
    sorted_data: list[dict] = sorted(data, key=lambda x:x['Date'])
    
    # add new index to events
    i = 1
    for row in sorted_data:
        row['ID'] = i
        i +=1
    
    return sorted_data

#writes data to csv
#returns None
def write(file_name: str, data: list[dict]) -> None:
    with open(file_name, mode = 'w', newline = '') as outfile:
        fieldnames: list[str] = data[0].keys()
        csv_writer = csv.DictWriter(outfile, fieldnames = fieldnames)
        
        csv_writer.writeheader()
        csv_writer.writerows(data)

def update_csvfile(file_name: str) -> Optional[list[dict]]:
    file_data = read_and_parse_data('tasks.csv')

    correct_data = sort_and_add_index(file_data)
    if correct_data != None:
        write('tasks.csv', correct_data)
        return correct_data
    return None

# removes choosen task
#return None : wrong key, data doesnt exist, task doesnt exist
def remove_task(id_to_remove: int, file_name: str) -> Optional[dict]:
    #to avoid accidental mistakes
    if not confirmation():
        print("Wrong key, task was not delated")
        return None
    
    data = update_csvfile(file_name)
    if data == None:
        print("Lack of data")
        return None

    update_data = [row for row in data if int(row['ID']) != id_to_remove]
    removed_task = [row for row in data if int(row['ID']) == id_to_remove]

    write(file_name, update_data)

    update_csvfile(file_name)

    try:
        return removed_task[0]
    except:
         print("This task doesn't exist")
         return None


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
    
     
def automatic_deletion(file_name) -> Optional[list[dict]]:
    data = update_csvfile(file_name)
    tasks_to_remove: list = []

    if data != None:
        for row in data:     
            diff: int = (row['Date'].date() - datetime.today().date()).days
            if diff < 0:
                tasks_to_remove.append(row['ID'])  

    update_data = [row for row in data if row['ID'] not in tasks_to_remove]
    removed_tasks = [row for row in data if row['ID'] in tasks_to_remove]
        
    write(file_name, sort_and_add_index(update_data))


def additional_date(data: list[dict]) -> Optional[list[dict]]:
    for row in data:
        row["Day_of_week"] = row['Date'].strftime("%A")
        row["Difference"] = (row['Date'].date() - datetime.today().date()).days
    return data


def get_data(file_name) -> Optional[list[dict]]:
    data = update_csvfile(file_name)
    return additional_date(data)
    

# function changes the state of task; returns current state of event 
def done_undone(id_to_change: int | list[int], file_name: str = 'tasks.csv') -> None:
    data = update_csvfile(file_name)

    if type(id_to_change) == int:
        print(data[id_to_change]['State'])
        data[id_to_change-1]['State'] = '1' if data[id_to_change-1]['State'] == '0' else '0'
    else:
        for id in id_to_change:
            data[id-1]['State'] = '1' if data[id-1]['State'] == '0' else '0'

    write(file_name, data)



def edit_task(id: int, key: str, update_value: str, file_name: str = 'tasks.csv') -> Optional[dict]:
    check_key = ['name','date','description']
    if key.lower() not in check_key:
        
        print(key.lower())
        return None
    

    data = update_csvfile(file_name)
    if data == None:
        print("Lack of data")
        return None
    try:
        match key.lower():
            case 'name' | 'description':
                data[id-1][key.capitalize()] = update_value
            case 'date':
                data[id-1][key.capitalize()] = datetime.strptime(update_value, "%Y-%m-%d %H:%M:%S")
    except IndexError:
        print("This task doesn't exist")
        return None

    write(file_name, data)
    if key.lower() == 'date':
        update_csvfile(file_name)

    return data[id-1]

if __name__ == "__main__":
    # print(automatic_deletion('tasks.csv'))
    # # remove_task(4, 'tasks.csv')
    # done_undone(4)
    # done_undone([2,3,5])
    # print(update_csvfile('tasks.csv'))
    # edit_task(3, 'Date', '2024-02-02 00:00:00')
    # print(edit_task(3, 'description', 'write_new_code'))
    ...

