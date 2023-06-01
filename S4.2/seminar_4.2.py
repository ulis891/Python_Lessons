# text = 'aaabcaadcdd'
# new_text = []
# for i in text:
#     if i not in new_text:
#         new_text.append(i)
#     else:
#         new_text.append(i)
#         new_text.append('_' + str(new_text.count(i)-1))
# print("".join(new_text))


text = "Привет, как дела? привет, милая. привет, любимая! привет, дорогая".replace(
                                                                                    '!', '').replace(
                                                                                    '?', '').replace(
                                                                                    '.', '').replace(
                                                                                    ',', '').lower(
                                                                                    ).split()
# buffer_text = []
# for word in text:
#     if word not in buffer_text:
#         buffer_text.append(word)

print(len(set(text)))
