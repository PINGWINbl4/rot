alpabet = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x = str(input('Введите сообщение на английском языке'))
x = x.lower()
x = list(x)
p = True
try:
    while p:
        dlina = len(x)
        if " " in x:
            x.remove(' ')
        for i in range(dlina):
            if x[i] in alpabet:
                p = False
            else:
                x = str(input('Сообщение некорректно, введите новое'))
                dlina = len(x)
                if " " in x:
                    x.remove(' ')
                x = x.lower()
                x = list(x)
                p = True
except(IndexError):
    dlina = len(x)
    p = True

print('rot = ')
rot = int(input())
for i in range(len(x)):
    d = 0
    while alpabet[d] != x[i]:
        d += 1

    x[i] = alpabet[(d+rot) % 26]
print('Ваша закодированная строка',*x)