import re

f = open('emd.csv',encoding="utf8")
next(f)

modalidades = {}

for line in f:
    campos = re.split(',', line)
    m = campos[8]
    if m in modalidades:
        modalidades[m] += 1
    else:
        modalidades[m] = 1

print(sorted(modalidades))
print(sorted(modalidades.items()))
print(dict(sorted(modalidades.items(), key=lambda p: p[0])))
print(dict(sorted(modalidades.items(), key=lambda p: p[1])))

print()
#print('Numero de modalidades: ' + str(len(modalidades)))
print('Numero de modalidades: ', len(modalidades))

f.close()
