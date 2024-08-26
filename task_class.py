import csv
import datetime



# class event creates events
class Task:
    def __init__(self, name: str, year: int, month: int, day: int,  hour: int = 0, minute: int = 0, description: str = '', add_to_file: bool = True):
        self.name = name
        self.data = datetime.datetime(year, month, day, hour, minute)
        self.description = description
        self.id = self.generate_id()
        self.state: int = 0
        if add_to_file == True:
            self.add_event()


    # add_event method adds event to the csv file 
    def add_event(self):
        new_event = {'ID': self.id,'Name': self.name, 'Date': self.data, 'Description': self.description, 'State': self.state}

        with open('events.csv', mode = 'a', newline='') as file:
            fieldnames = ['ID','Name','Date', 'Description', 'State']

            csv_writer = csv.DictWriter(file, fieldnames = fieldnames)
            
            csv_writer.writerow(new_event)

    # generate_id method adds number to an event
    @classmethod
    def generate_id(cls):
        with open('events.csv', mode = 'r') as file:

            csv_reader = csv.DictReader(file)
            
            k = 0
            for row in csv_reader:
                k = row['ID']
            cls.c_id = int(k)+1

        return cls.c_id  
    
    





