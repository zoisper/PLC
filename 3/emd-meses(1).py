import re



f = open('emd.csv')
next(f)

meses = {}

for line in f:
    campos = re.split(r',', line)
#    mes = re.search(r'(\d+-\d+)-\d+', campos[2])[1]
    mes = re.search(r'\d+-(\d+)-\d+', campos[2])[1]
    if mes in meses:
        meses[mes] += 1
    else:
        meses[mes] = 1

meses = dict(sorted(meses.items(), key=lambda p: p[0]))
print(meses)

f.close()
