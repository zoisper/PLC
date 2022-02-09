import re


f = open('emd.csv',encoding="utf8")
next(f)

clubes = set()

for line in f:
    campos = re.split(',', line)
    clubes.add(campos[9])


print(sorted(clubes))
print('Numero de clubes: ' + str(len(clubes)))

f.close()
