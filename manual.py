from typing import Dict, List


class Manual:
    fn_descriptions: Dict[str, str] = {
        "help": "display overview of current functionalities of the app",
        "display_events" : "display otherview of exisiting events",
        "display_events_by_date" : "display otherview of exisiting events on the selected day or range of days",
        "add_event" : "allows user to add event",
        "remove_event" : "allows user to remove selected event ",
        "edit_event" : "allows user to change features of selected event"
        
    }

    fn_invokes: Dict[str, str] = {
        "help" : "no args needed || str fn_name"
    }
