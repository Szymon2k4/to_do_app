from typing import Dict, List
from update_and_read_tasks import get_data, remove_task, edit_task, done_undone
from task_class import Task
from datetime import datetime
from display_tasks import display_all_tasks


class App:
    running : bool
    stored_data: List[Dict]


    def __init__(self):
        self.running = True
        self.stored_data = get_data()
    
    def run(self):
        self.handle_input()

    def handle_input(self, input_text: str):
        try:
            command: str = input()
            command = self.parse_input(command)
        except KeyboardInterrupt:
            self.running = False
    

    def handle_command(self, cmd: str, args: list):
        match cmd:
            case "help":
                ...
            case "add_task":
                self.handle_add_task()
            case "display_task":
                self.handle_diplay_tasks()
            case "remove_task":
                self.handle_remove_task()
            case "edit_task":
                self.handle_edit_task()
            case "change_state":
                self.handle_done_undone()
            case  _:
                ...

    def handle_add_task(self):
        print("New task: ")

        name: str = self.handle_input("Name: ")

        date: str = self.handle_input("Date YYYY-MM-DD: ")
        check_date = date + ' 00:00'
        wrong = True
        while wrong:
            try:
                datetime.strptime(check_date, "%Y-%m-%d %H:%M")
                wrong = False
            except ValueError:
                print("Enter correct format")
                date: str = self.handle_input("Date [YYYY-MM-DD]: ")
        year, month, day = date.split('-')

        time: str = self.handle_input("Time [HH:MM]: ")
        check_date = date + time
        while wrong:
            try:
                datetime.strptime(check_date, "%Y-%m-%d %H:%M")
                wrong = False
            except ValueError:
                print("Enter correct format")
                date: str = self.handle_input("Time [HH:MM]: ")

        hour, minute = time.split(':')
        description: str = input("Description: ")

        new_task = Task(name, int(year), int(month), int(day), int(hour), int(minute), description)

    def handle_diplay_tasks(self) -> None:
        raise NotImplementedError
    
    def handle_remove_task(self) -> None:
        display_all_tasks('tasks.csv')
        print("\n")
        id: int = int(self.handle_input("Enter ID of task you want to remove: "))

        remove_task(id, 'tasks.csv')
    
    def handle_edit_task(self) -> None:
        display_all_tasks('tasks.csv')
        print("\n")
        id: int = int(self.handle_input("Enter ID of task you want to edit: "))
        key: str = self.handle_input("What do you want to change [date, name, description]: ")
        update_value: str = self.handle_input("Enter new value: ")


        edit_task(id, key, update_value, 'tasks.csv')


    @staticmethod
    def handle_done_undone(self) -> None:
        display_all_tasks('tasks.csv')
        print("\n")
        id = int(self.handle_input("Enter id of task you want to change state: "))

        done_undone(id, 'tasks.csv')




    def parse_main_input(self, cmd: str) -> str:
        return cmd.strip().lower()