"""Напишите программу, удаляющую из текста все слова, содержащие "абв"."""

fragment = 'абв'

words = ''
with open('text.txt', 'r', encoding='utf-8') as text:
    for line in text:
        words += line
words = words.replace('\n', ' ').split(' ')

new_list = []
for word in words:
    if fragment not in word:
        if word.istitle():
            word = "\n" + word
        new_list.append(word)

print(' '.join(new_list))

