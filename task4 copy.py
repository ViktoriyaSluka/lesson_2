list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(list)):
    name = list[i].split(' ')[-1]
    name = name.lower().capitalize()
    x = len(list[i]) - 1
    while x >= 0:
        if x > 0 and list[i][x-1].isspace():
            list[i] = list[i][:x] + name
            print("Привет,", name)
            break
        x -= 1
print(list)



'''
list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
new_list = [elem.strip().split(',') for elem in list]
print(new_list)
for tuple_element in list[::1]:
    print(tuple_element.split())
    '''

"""
i = 0
if tuple_element.isupper(i):
    print(tuple_element.lower(i))
    i +=1
"""

'''
i = 0
while i < len(list):
    list_split = list.split()
'''
#print(help(list))
#print(list_split)





'''for i in range(10):
    list.split(str(-1))
print(''.join(list))
'''