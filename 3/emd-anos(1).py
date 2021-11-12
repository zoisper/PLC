import re

f = open('emd.csv',encoding="utf8")
next(f)

anos = {}

for line in f:
    campos = re.split(r',', line)

    genero = campos[6]
    if genero == 'F':
        ano = re.split(r'-', campos[2])[0]
        if ano in anos:
            anos[ano] += 1
        else:
            anos[ano] = 1

print(dict(sorted(anos.items(), key=lambda e: e[0])))

f.close()
