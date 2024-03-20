f = open('hivas.txt', 'rt', encoding='utf-8')

def mpbe(h, m, s):
    return ((h * 60) + m) * 60 + s

stat = {}
masodpercek = []
munkaido_hivasok = []
beszelok = []
for sor in f:
    tmp = sor.strip().split(' ')
    keys = stat.keys()
    if tmp[0] in keys:
        stat[tmp[0]] += 1
    else:
        stat[tmp[0]] = 1
    masodpercek.append((mpbe(int(tmp[3]),int(tmp[4]),int(tmp[5]))) - (mpbe(int(tmp[0]),int(tmp[1]),int(tmp[2]))))
    if int(tmp[3]) >= 8 and int(tmp[0]) < 12:
        munkaido_hivasok.append(tmp)

print("3. feldat")
for k,v in stat.items():
    print(k,"óra", v, "hívás")

print('4. feladat')
mpszamlalo = 0
for i in masodpercek:
    if i > mpszamlalo:
        mpszamlalo = i
hely = masodpercek.index(mpszamlalo) + 1
print(f'A leghosszabb ideig vonalban lévő hívó {hely}. sorban szerepel,')
print(f'A hívás hossza: {mpszamlalo} másodperc.')

print('5. feladat')
idopont = input('Adjon meg egy időpontot! (óra perc másodperc)')
ido = idopont.split(' ')
while int(ido[0]) < 8 or int(ido[0]) > 12:
    idopont = input('Adjon meg egy időpontot! (óra perc másodperc)')
    ido = idopont.split(' ')

beszelok.append(munkaido_hivasok[0])
for i in range(1, len(munkaido_hivasok)):
    


print('temp', munkaido_hivasok)
print('beszel', beszelok)