import re


f = open('emd.csv',encoding="utf8")
next(f)

d = { 'M': 0, 'F': 0 }

for line in f:
    campos = re.split(r',', line)
    d[campos[6]] += 1

print('Masculino:', d['M'])
print('Feminino:', d['F'])

f.close()
