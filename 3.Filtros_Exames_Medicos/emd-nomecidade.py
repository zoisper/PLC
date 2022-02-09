import re

f = open('emd.csv',encoding="utf8")
next(f)

for line in f:
    campos = re.split(r',', line)
    primeiro_nome = campos[3]
    ultimo_nome = campos[4]
    cidade = campos[7]
    
    print(primeiro_nome, ultimo_nome, cidade)


f.close()
