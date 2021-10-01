alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))
alphabet.append(' ')

string = str(input('Сообщение на английском'))
string.lower()
dlina = len(string)

for i in range(dlina):
    if string[i] not in alphabet:
        string = str(input('Строка не корректна'))
        string.lower()
        i = 0
        dlina = len(string)

while True:
    try:
        rot = int(input("введите сдвиг"))
        break
    except(ValueError):
        print('Некорректное значение')

for i in range(len(string)):
    if string[i] != ' ':
        char = (ord(string[i])+rot)
        if char > 122:
            char -= 26
        print(chr(char), end='')
    else:
        print(' ')
