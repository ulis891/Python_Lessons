"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных."""

with open('original_text.txt') as original:
    for text in original:
        original_text = text

encrypted_list = []

try:
    count = 1
    for i in range(len(original_text)):
        if original_text[i] == original_text[i + 1]:
            count += 1
        else:
            encrypted_list.append(original_text[i] + str(count))
            count = 1
except IndexError:
    encrypted_list.append(original_text[i] + str(count))

encrypted_text = ''
for code in encrypted_list:
    encrypted_text += code

with open('encrypted_text.txt', 'w') as en_text:
    print(encrypted_text, file=en_text)

decrypted_text = ''
letter_buffer = ''

with open('encrypted_text.txt') as en_text:
    for code in en_text:

        for i in code:
            if i.isdigit():
                count += i
            else:
                if count != '':
                    decrypted_text += letter_buffer * int(count)
                    count = ''
                    letter_buffer = i
                else:
                    letter_buffer = i

with open('decrypted_text.txt', 'w') as de_text:
    print(decrypted_text, file=de_text)

print(f'\n{original_text}')
print(f'длинна изначального текста: {len(original_text)} знаков\n')

print(f'зашифрованный текст:\n{encrypted_text}\n')

print(decrypted_text)
print(f'длина разшифрованного текста: {len(decrypted_text)} знаков')
