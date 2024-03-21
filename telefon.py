f = open('hivas.txt', 'rt', encoding='utf-8')

def mpbe(h, m, s):
    return ((h * 60) + m) * 60 + s

stat = {}
masodpercek = []
munkaido_hivasok = []
beszelok = []
sorszam = 1
for sor in f:
    tmp = sor.strip().split(' ')
    tmp.append(sorszam)
    sorszam += 1
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
eppen_hivasba_varakozok = []
for i in range(len(munkaido_hivasok)):
    if mpbe(int(ido[0]), int(ido[1]), int(ido[2])) > mpbe(int(munkaido_hivasok[i][0]), int(munkaido_hivasok[i][1]), int(munkaido_hivasok[i][2])) and mpbe(int(ido[0]), int(ido[1]), int(ido[2])) < mpbe(int(munkaido_hivasok[i][3]), int(munkaido_hivasok[i][4]), int(munkaido_hivasok[i][5])):
        eppen_hivasba_varakozok.append(munkaido_hivasok[i])
print(f'A várakozók száma: {len(eppen_hivasba_varakozok)-1} a beszélő a {eppen_hivasba_varakozok[0][6]}. hívó.')


print('6. feladat')
beszelok.append(munkaido_hivasok[0])
for i in range(1, len(munkaido_hivasok)):
    
    elozo_hivas = beszelok[-1]
    if mpbe(int(elozo_hivas[3]), int(elozo_hivas[4]), int(elozo_hivas[5])) < mpbe(int(munkaido_hivasok[i][3]), int(munkaido_hivasok[i][4]), int(munkaido_hivasok[i][5])):
        temp = munkaido_hivasok[i]
        temp.append(elozo_hivas[3])
        temp.append(elozo_hivas[4])
        temp.append(elozo_hivas[5])
        beszelok.append(temp)
        
print(f'Az utolsó telefonáló adatai a(z) {beszelok[-1][6]}. sorban vannak, {mpbe(int(beszelok[-1][7]), int(beszelok[-1][8]), int(beszelok[-1][9])) - mpbe(int(beszelok[-1][0]), int(beszelok[-1][1]), int(beszelok[-1][2]))} másodpercig várt.')

