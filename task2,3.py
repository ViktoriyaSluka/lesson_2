list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print("List before", list)
i = 0
while i < len(list):
    if list[i].lstrip("+-").isdigit():
        list.insert(i, '"')
        i += 1
        if list[i][0] in '+-':
            list[i] = list[i][0] + list[i][1:].zfill(2)
        else:
            list[i] = list[i].zfill(2)
        list.insert(i + 1, '"')
    i += 1

print("List after", list)

stl = ""
for i in list:
    if i.isalpha():
        stl += ''.join(f'{" "}{str(i)}{" "}')
    else:
        stl += ''.join(str(i))
stl = stl.lstrip(stl[0])
stl = stl.rstrip(stl[-1])
print("String from list:", stl)