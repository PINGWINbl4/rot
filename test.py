alphabet = []
for i in range(97, 123):    # Формирование алфавита
    alphabet.append(chr(i))
alphabet.append(' ')

string = str(input('Сообщение на английском')) # Обработка строки в нужном формате
string.lower()
dlina = len(string)

for i in range(dlina):  # Проверка строки на нахождение в алфавите
    if string[i] not in alphabet:
        string = str(input('Строка не корректна'))
        string.lower()
        i = 0
        dlina = len(string)

while True:     # Ввод сдвига и проверка его на ошибки ввода
    try:
        rot = int(input("введите сдвиг"))
        break
    except(ValueError):
        print('Некорректное значение')

for i in range(len(string)): #Реализация сдвига эллемента строки в соответствии с алфавитом
    if string[i] != ' ':
        char = (ord(string[i])+rot)
        if char > 122:
            char -= 26
        print(chr(char), end='')
    else:
        print(' ')