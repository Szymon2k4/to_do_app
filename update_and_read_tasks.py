import csv
from datetime import datetime
from typing import Optional
from random import randint


#get data from csv file
def read(file_name: str) -> Optional[list[dict]]:
    with open (file_name, mode = 'r') as file:
        csv_reader: csv.DictReader = csv.DictReader(file)
        rows: list[dict] = [row for row in csv_reader]

    # return 0 if data does not exist
    if rows == []:
         return None
    return rows


def parse_data(data: list[dict]) -> list[dict]:
    for row in data:
        row['Date'] = datetime.strptime(row['Date'], "%Y-%m-%d %H:%M:%S")
        row['ID'] = int(row['ID'])
        
        

    # sort data by date
    parsing_data: list[dict] = sorted(data, key=lambda x:x['Date'])
    
    # add new index to events
    i = 1
    for row in parsing_data:
        row['ID'] = i
        i +=1
    
    return parsing_data

def read_and_parse_data(file_name: str) -> Optional[list[dict]]:
    data = read(file_name)
    data = parse_data(data)
    return data


def write(file_name: str, data: list[dict]) -> None:
    with open(file_name, mode = 'w', newline = '') as outfile:
        fieldnames: list[str] = data[0].keys()
        csv_writer = csv.DictWriter(outfile, fieldnames = fieldnames)
        
        csv_writer.writeheader()
        csv_writer.writerows(data)


def remove_task(id_to_remove: int, file_name: str) -> Optional[dict]:

    if not confirmation():
        return None

    if read(file_name) == None:
        return None
    
    data = read(file_name)
    if data == None:
        return None

    update_data = [row for row in data if int(row['ID']) != id_to_remove]
    removed_task = [row for row in data if int(row['ID']) == id_to_remove]

    write('events.csv', parse_data(update_data))

    try:
        return removed_task[0]
    except:
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
    
     
def automatic_deletion(file_name) -> None:
    data = read_and_parse_data(file_name)

    current_data = additional_date(data)
    tasks_to_remove: list = []

    if data != None:
        for row in current_data:     
            if int(row["Difference"]) < 0:
                tasks_to_remove.append(row['ID'])  

        remove_some_tasks(tasks_to_remove, file_name)


def remove_some_tasks(ids_to_remove: list[int], file_name: str) -> Optional[list[dict]]:
    read(file_name)
    
    data = read(file_name)
    if data == None:
        return None

    update_data = [row for row in data if int(row['ID']) not in ids_to_remove]
    removed_tasks = [row for row in data if int(row['ID']) in ids_to_remove]

    write('events.csv', parse_data(update_data))

    try:
        return removed_tasks
    except:
         return None
    
    
def additional_date(data: list[dict]) -> Optional[list[dict]]:
    for row in data:
        row["Day_of_week"] = row['Date'].strftime("%A")
        row["Difference"] = (row['Date'].date() - datetime.today().date()).days
        print(row["Difference"])
    return data


def update_csvfile(file_name) -> Optional[list[dict]]:
    automatic_deletion('events.csv')
    file_data = read('events.csv')

    if file_data != None:
        parsing_data = parse_data(file_data)
        write('events.csv', parsing_data)
        return parsing_data 
    return None


def get_data(file_name) -> Optional[list[dict]]:
    data = update_csvfile(file_name)
    return additional_date(data)
    



if __name__ == "__main__":
    print(automatic_deletion('events.csv'))
    remove_task(4, 'events.csv')
