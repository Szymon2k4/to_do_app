# from datetime import datetime
# array = []

# array = sorted(array)

# print(array)

# print(type(4))
# print(type([1, 2]))


# a = 2
# b = [1,2]
# if type(b) == list:
#     print("ok")

# print('a') if a in b else print('bbb')

# x = "2024-4"
# y, z  = x.split('-')
# print(y)
# print(z)

# date = '2024-3-3'
# date = date + ' 00:00'
# print(date)
# date_1 = datetime.strptime(date, "%Y-%m-%d %H:%M")
# print(date_1)

# l = '01'
# print(int(l))

# st = 'ania ma      kota  '
# st = st.strip().lower().split()
# sen = ' '.join(st)
# print(sen)

# fn_descriptions = {
#         "help": "display overview of current functionalities of the app",
#         "add_task" : "allows user to add event",
#         "display_tasks" : "display otherview of exisiting events",
#         "remove_task" : "allows user to remove selected task ",
#         "edit_task" : "allows user to change features of selected event",
#         "change_state" : "allows user to change state [done|undone]"
#     }

# print(fn_descriptions.keys()[1])

def parse_input(cmd: str, main_func = True) -> str:
        sentence_list:list[str] = [word for word in cmd.strip().lower().split()]
        return '_'.join(sentence_list)
    
print(parse_input('add task'))