# This is a sample Python script.

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # 'a' - данные дописываются, 'w' - данные перезаписываются
#data.writelines(colors) # Разделителей не будет
data.write('\nLINE 2\n')
data.write('LINE 3\n')
data.close()



path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
