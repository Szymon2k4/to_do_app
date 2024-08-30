from update_and_read_tasks import get_data

def display_all_events(file_name: str, change = True):
    rows = get_data(file_name)
    print('')
    if (change):
        print("ID  NAME                              DATE              TIME          DAY_OF_WEEK    DAYS         STATE")
        for row in rows:
            print(f"{str(row['ID']).ljust(2)}  {row['Name'].ljust(30)}||  {str(row['Date'])[:10].ljust(16)} {str(row['Date'])[10:16].ljust(10)} ||  {row['Day_of_week'].ljust(11)} || {str(row["Difference"]).ljust(5)}        {'done' if row['State'] == '1' else 'not done'}")
    else:
        print(" NAME                              DATE              TIME          DAY_OF_WEEK    DAYS")
        for row in rows:
            print(f" {row['Name'].ljust(30)}||  {str(row['Date'])[:10].ljust(16)} {str(row['Date'])[10:16].ljust(10)} ||  {row['Day_of_week'].ljust(11)} || {str(row["Difference"]).ljust(5)}")

display_all_events('events.csv')