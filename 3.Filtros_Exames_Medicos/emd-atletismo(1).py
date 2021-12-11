import re

f = open('emd.csv',encoding="utf8")
next(f)

atletas = []
for line in f:
    campos = re.split(',', line)
    if campos[8] == 'Atletismo':
        atletas.append((campos[3] + ' ' + campos[4], campos[5]))


atletas.sort(key=lambda p: (p[1], p[0]))
print(atletas)

f.close()
