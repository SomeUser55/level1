
END = '\n\n'

# Вывести последнюю букву в слове
word = 'Архангельск'
last_char = word[-1]
print('последняя буква в слове {!r} = {}'.format(word, last_char), end=END)


# Вывести количество букв "а" в слове
word = 'Архангельск'
a_char_count = word.lower().count('а')
print('количество букв "а" в слове {!r} = {}'.format(word, a_char_count), end=END)


VOWELS = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е'] 
# Вывести количество гласных букв в слове
word = 'Архангельск'
cnt = 0
for char in word.lower():
    if char in VOWELS:
        cnt += 1

print('количество гласных букв в слове {!r} = {}'.format(word, cnt), end=END)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words_count = len(sentence.split())
print('количество слов в предложении {!r} = {}'.format(sentence, words_count), end=END)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print('первая буква каждого слова в {!r}:'.format(sentence)) 
for word in sentence.split():
    print('{:>4}'.format(word[0]))

print('\n')


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = sentence.split()
words_len = [len(word) for word in words]
words_count = len(words) 
avg_word_len = sum(words_len) / words_count
print('Средняя длина слова: {}'.format(avg_word_len), end=END)