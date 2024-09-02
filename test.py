from datetime import datetime
array = []

array = sorted(array)

print(array)

print(type(4))
print(type([1, 2]))


a = 2
b = [1,2]
if type(b) == list:
    print("ok")

print('a') if a in b else print('bbb')

x = "2024-4"
y, z  = x.split('-')
print(y)
print(z)

date = '2024-3-3'
date = date + ' 00:00'
print(date)
date_1 = datetime.strptime(date, "%Y-%m-%d %H:%M")
print(date_1)

l = '01'
print(int(l))