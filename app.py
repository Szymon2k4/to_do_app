from typing import Dict, List
from get_data_from_csv import get_data


class App:
    running : bool
    stored_data: List[Dict]


    def __init__(self):
        self.running = True
        self.stored_data = get_data()
    
    def run(self):
        self.handle_input()

    def handle_main_input(self):
        try:
            command: str = input()
            command = self.parse_input(command)
        except KeyboardInterrupt:
            self.running = False
    

    def handle_command():
        pass
    
    def parse_input(self, cmd: str) -> str:
        return cmd.strip().lower()