alpabet = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x = str(input())
print('rot = ')
rot = int(input())
x = x.lower()
x = list(x)
if " " in x:
    x.remove(' ')
for i in range(len(x)):
    d = 0
    while alpabet[d] != x[i]:
        d += 1
        if d == 25:
            d = 0
    x[i] = alpabet[(d+rot) % 26]
print(x)
