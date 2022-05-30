my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print("My list before", my_list)
i = 0
while i < len(my_list):
    if my_list[i].lstrip("+-").isdigit():
        my_list.insert(i, '"')
        i += 1
        if my_list[i][0] in '+-':
            my_list[i] = my_list[i][0] + my_list[i][1:].zfill(2)
        else:
            my_list[i] = my_list[i].zfill(2)
        my_list.insert(i + 1, '"')
    i += 1

print("My list after", my_list)

stl = ""
for i in my_list:
    if i.isalpha():
        stl += ''.join(f'{" "}{str(i)}{" "}')
    else:
        stl += ''.join(str(i))
stl = stl.lstrip(stl[0])
stl = stl.rstrip(stl[-1])
print("String from my list:", stl)