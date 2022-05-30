my_list = [3.05, 5, 3.14, 6, 7, 53.2, 5.5, 1, 1, 8.7]
#1
def print_price(my_list):
    for i in range(len(my_list)):
        rub = int(my_list[i])
        cop = round(100*(my_list[i] % 1))

        if i == len(my_list) - 1:
            print(rub, 'руб', f'{cop:02}', 'коп')
        else:
            print(rub, 'руб', f'{cop:02}', 'коп', end=', ')

print_price(my_list)
#2
my_list.sort()
print_price(my_list)
#3
reverse_list = sorted(my_list, reverse=True)
print_price(reverse_list)
#4
print_price(my_list[-5:])