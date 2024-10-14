from typing import Dict, List
from update_and_read_tasks import get_data, remove_task, edit_task, done_undone, read_and_parse_data
from task_class import Task
from datetime import datetime
from display_tasks import display_all_tasks
from typing import Optional
from manual import Manual
from time import sleep

# sss

class App:
    running : bool
    stored_data: List[Dict]


    def __init__(self) -> None:
        self.running = True


    def run(self) -> None:
        self.handle_input(in_main_func = True)


    def handle_input(self, input_text: str = '', in_main_func:bool = False) -> Optional[str]:
        try:
            if in_main_func:
                print("*ACTION*: ", end = '')
            try:
                command: str = input(input_text)
            except (KeyboardInterrupt, UnboundLocalError):
                self.running
            if in_main_func:
                command = self.parse_input(command)
                if command in Manual.commands:
                    self.handle_command(command)
                else:
                    print("WRONG")
            else:
                return command
        except KeyboardInterrupt:
            self.running = False
    

    def handle_command(self, cmd: str):
        match cmd:
            case "help":
                Manual.help()
            case "add_task":
                self.handle_add_task()
            case "display_tasks":
                self.handle_diplay_tasks()
            case "remove_task":
                self.handle_remove_task()
            case "edit_task":
                self.handle_edit_task()
            case "change_state":
                self.handle_done_undone()
            case "exit":
                self.handle_exit()
            case  _:
                ...


    def handle_add_task(self):
        print("\n"+"%"*28+" ADD TASK "+"%"*28)
        print("\nCREATE NEW TASK:\n")

        name: str = self.handle_input("NAME: ")

        while True:
            date: str = self.handle_input("DATE YYYY-MM-DD: ")
            if self.date_format(date):
                break
            else:
                print("Enter correct date format")
        year, month, day = date.split('-')

        description: str = input("DESCRIPTION: ")

        new_task = Task(name, int(year), int(month), int(day), description)
        print("\nTASK SUCCESSFULLY CREATED!")
        print("\n"+"%"*66+"\n")


    def handle_diplay_tasks(self) -> None:
        display_all_tasks('tasks.csv')
    

    def handle_remove_task(self) -> None:
        if not self.data_exits():
            print("THERE IS NO DATA")
            return
        print("\n"+"!"*27+" REMOVE TASK "+"!"*26)
        display_all_tasks('tasks.csv')
        while True:
            try:
                id: int = int(self.handle_input("Enter ID of task you want to remove: "))
                break
            except ValueError:
                print("Enter number")

        if remove_task(id, 'tasks.csv') is not None:
            print("\nTASK SUCCESSFULLY REMOVED!")
        else:
            print("\nUNSECCESSEFUL ACTION")
        print("\n"+"!"*66+"\n")


    def handle_edit_task(self) -> None:
        if not self.data_exits():
            print("THERE IS NO DATA")
            return
        print("\n"+"+"*28+" EDIT TASK "+"+"*27)
        display_all_tasks('tasks.csv')


        while True:
            try:
                id: int = int(self.handle_input("Enter ID of task you want to edit: "))
                if not self.exist(id, read_and_parse_data()):
                    print("\nTASK DOESN'T EXIST")
                    print("\nUNSECCESSEFUL ACTION")
                    print("\n"+"+"*66+"\n")
                    return
                break
            except ValueError:
                print("Enter number")
        keys_list = ['date', 'name', 'description']
        while True:
            try:
                key: str = self.handle_input("What do you want to change [date, name, description]: ")
                key = self.parse_input(key)
                if key in keys_list:
                    break
                else:
                    print("Enter correct key")
            except UnboundLocalError:
                print("Enter correct key")

        if key == 'date':
            while True:
                update_value: str = self.handle_input("Enter new value[YYYY-MM-DD]: ")
                if self.date_format(update_value):
                    break
                else:
                    print("Enter correct date format")
        else:
            update_value: str = self.handle_input("Enter new value: ")
            



        if edit_task(id, key, update_value, 'tasks.csv') is not None:
            print("\nTASK SUCCESSFULLY EDITED!")
        else:
            print("\n UNSECCESSEFUL ACTION")
        print("\n"+"+"*66+"\n")


    def handle_done_undone(self) -> None:
        if not self.data_exits():
            print("THERE IS NO DATA")
            return
        print("\n"+"&"*26+" CHANGE STATE "+"&"*26)
        display_all_tasks('tasks.csv')
        print("\n")
        while True:
            try:
                id = int(self.handle_input("Enter id of task you want to change state: "))
                break
            except:
                print("Enter correct number")

        done_undone(id, 'tasks.csv')

        print("\nSTATE SUCCESSFULLY CHANGED!")
        print("\n"+"&"*66+"\n")

    def handle_exit(self):
        print("\nshutdown...\n")
        sleep(1)
        self.running = False


    @staticmethod
    def parse_input(cmd: str) -> str:
        sentence_list:list[str] = [word for word in cmd.strip().lower().split()]
        return '_'.join(sentence_list)
    

    @staticmethod
    def date_format(date: str):
        check_date = date
        try:
            datetime.strptime(check_date, "%Y-%m-%d")
            return True
        except ValueError:
            return False
        

    @staticmethod
    def exist(id: int, data: List[dict]) -> bool:
        exist = [row for row in data if row['ID'] == id]
        try:
            exist[0]
            return True
        except IndexError:
            return False
        
    @staticmethod
    def data_exits() -> bool:
        if read_and_parse_data() == []:
            return False
        return True

        

