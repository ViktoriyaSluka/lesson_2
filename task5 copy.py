list = [3.05, 5, 3.14, 6, 7, 53.2, 5.5, 1, 1, 8.7]
#1
def print_price(list):
    for i in range(len(list)):
        rub = int(list[i])
        cop = round(100*(list[i] % 1))
        if i == len(list) - 1:
            print(rub ,'руб', f'{cop:02}', 'коп')
        else :
            print(rub ,'руб', f'{cop:02}', 'коп', end=', ')

print_price(list)
#2
list.sort()
print_price(list)
#3
reverse_list = sorted(list, reverse=True)
print_price(reverse_list)
#4
print_price(list[-5:])