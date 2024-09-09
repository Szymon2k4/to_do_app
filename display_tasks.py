from update_and_read_tasks import get_data
from time import sleep

def display_all_tasks(file_name: str):
    rows = get_data(file_name)
    print("\nID  NAME                              DATE                      DAY_OF_WEEK        DAYS         STATE")
    for row in rows:
        print(f"{str(row['ID']).ljust(2)}  {row['Name'].ljust(30)}||  {str(row['Date'])[:10].ljust(10)} {str(row['Date'])[10:16].ljust(10)} ||  {row['Day_of_week'].ljust(15)} || {str(row["Difference"]).ljust(5)}     ||  {'done' if row['State'] == '1' else 'not done'}")
        sleep(0.05)
    print('')
if __name__ == '__main__':
    display_all_tasks('events.csv')