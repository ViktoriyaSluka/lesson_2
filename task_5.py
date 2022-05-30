'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
"мягкий"]
Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
'''

import random


def get_jokes(number):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    joke = []
    for i in range(number):
        n = random.choice(nouns)
        ad = random.choice(adverbs)
        aj = random.choice(adjectives)
        joke.append(f'{n} {ad} {aj}')

    return joke


if __name__ == "__main__":
    print(get_jokes(3))
