import re

f = open('emd.csv',encoding="utf8")
next(f)

federados = 0
aprovados = 0

for line in f:
    campos = re.split(r',', line.strip())
    [fed, aprov] = campos[-2:]

    if fed == 'true':
        federados += 1
    if aprov == 'true':
        aprovados += 1

print('Federados:', federados)
print('Aprovados:', aprovados)

f.close()
