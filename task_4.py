my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(my_list)):
    name = my_list[i].split(' ')[-1]
    name = name.lower().capitalize()
    x = len(my_list[i]) - 1
    while x >= 0:
        if x > 0 and my_list[i][x-1].isspace():
            my_list[i] = my_list[i][:x] + name
            print("Привет,", name)
            break
        x -= 1
print(my_list)



'''
my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
new_list = [elem.strip().split(',') for elem in my_list]
print(new_list)
for tuple_element in my_list[::1]:
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
while i < len(my_list):
    list_split = list.split()
'''
#print(help(my_list))
#print(list_split)





'''for i in range(10):
    list.split(str(-1))
print(''.join(list))
'''