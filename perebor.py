alpabet = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x = str(input('Введите сообщение на английском языке'))
x = x.lower()
x = list(x)
p = True
while p:
    for i in range(len(x)):
        if x[i] in alpabet:
            p = False
        else:
            x = str(input('Сообщение некорректно, введите новое'))
            x = x.lower()
            x = list(x)
            p = True
print('rot = ')
rot = int(input())
if " " in x:
    x.remove(' ')
for i in range(len(x)):
    d = 0
    while alpabet[d] != x[i]:
        d += 1
        if d == 25:
            d = 0
    x[i] = alpabet[(d+rot) % 26]
print('Ваша закодированная строка',*x)