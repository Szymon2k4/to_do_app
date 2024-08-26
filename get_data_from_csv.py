import csv
from datetime import datetime
from remove_and_edit_event import remove_event
from typing import Optional

# function returns table of data if exists, otherwise returns None
def get_data() -> Optional[list[dict]]:
    with open ('events.csv', mode = 'r') as file:
        csv_reader = csv.DictReader(file)
        rows: list[dict] = [row for row in csv_reader]

    # return 0 if data does not exist
    if rows == []:
         return None
    
    # change type of some data
    for row in rows:
        row['Date'] = datetime.strptime(row['Date'], "%Y-%m-%d %H:%M:%S")
        row['ID'] = int(row['ID'])
        

    # sort data by date
    sorted_rows_by_date: list[dict] = sorted(rows, key=lambda x:x['Date'])
    
    # add new index to events
    i = 1
    for row in sorted_rows_by_date:
        row['ID'] = i
        i +=1
        

    # update events in csv file
    with open('events.csv', mode = 'w', newline = '') as outfile:
                fieldnames: list[str] = rows[0].keys()
                csv_writer = csv.DictWriter(outfile, fieldnames = fieldnames)
                
                csv_writer.writeheader()

                csv_writer.writerows(sorted_rows_by_date)


    # add more date based on existing data
    # remove expired events automaticly
    inaccurate_data: bool = False
    today = datetime.today().date()

    for row in sorted_rows_by_date:
        row["Difference"] = (row['Date'].date() - today).days
        if int(row["Difference"]) < 0:
             remove_event(row['ID'], automatic = True)
             inaccurate_data = True
        row["Day_of_week"] = row['Date'].strftime("%A")
    
    if inaccurate_data:
         sorted_rows_by_date = get_data()

    return sorted_rows_by_date




# test
if __name__ == "__main__":
    tab = get_data()
    if tab == 0:
        print("err")
    else:
        for row in tab:
            print(row)

