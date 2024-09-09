from typing import Dict, List


class Manual:
    fn_descriptions: Dict[str, str] = {
        "help": "display overview of current functionalities of the app",
        "add_task" : "allows user to add event",
        "display_tasks" : "display otherview of exisiting events",
        "remove_task" : "allows user to remove selected task ",
        "edit_task" : "allows user to change features of selected event",
        "change_state" : "allows user to change state [done|undone]",
        "exit" : " terminate app"
    }

    commands: List[str] = fn_descriptions.keys()


    @staticmethod
    def help() -> None:
        print("\n"+"*"*30+" HELP "+"*"*30)
        print("This app is used for managing your tasks. With it you will never forgot what you have to do.")
        print("After '*ACTIONS*:' type name of one of the functions depening on what you want to do\n")
        print("FUNCTIONS: \n")
        for fun in Manual.fn_descriptions.items():
            key, value = fun
            key = key.replace('_', ' ').upper()
            print(f"{key}:  {value}")
        print("\n"+"*"*66+"\n")
    
    @staticmethod
    def introduction() -> None:
        print("\n\n","="*20,"WELCOME TO THE 'TO_DO_APP'", "="*20,"\n")
        print("For more information about this app type 'help'")



if __name__ == '__main__':
    Manual.help()
    print(Manual.commands)
