'''
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
русский язык. Например:
#>>> num_translate("one")
"один"
#>>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
снаружи.
'''


def num_translate():
    translater = input("Введите число от 0 - 10 на английском: ")
    num_translate = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
                     "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять", }
    for key, valye in num_translate.items():
        if translater == key:
            print(valye)
    if translater not in num_translate:
        print("None")

if __name__ == "__main__":
    num_translate()
