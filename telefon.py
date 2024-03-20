f = open('hivas.txt', 'rt', encoding='utf-8')

def mpbe(h, m, s):
    return ((h * 60) + m) * 60 + s

stat = {}
for sor in f:
    tmp = sor.strip().split(' ')
    keys = stat.keys()
    if tmp[0] in keys:
        stat[tmp[0]] += 1
    else:
        stat[tmp[0]] = 1
print("3. feldat")
for k,v in stat.items():
    print(k,"óra", v, "hívás")

masodpercek = []
for sor in f:
    tmp = sor.strip().split(' ')
    masodpercek.append((mpbe(int(tmp[3]),int(tmp[4]),int(tmp[5]))) - (mpbe(int(tmp[0]),int(tmp[1]),int(tmp[2]))))
mpszamlalo = 0
for i in masodpercek:
    if i > mpszamlalo:
        mpszamlalo = i
hely = masodpercek.index(mpszamlalo) + 1
print('4. feladat')
print(f'A leghosszabb ideig vonalban lévő hívó {hely}. sorban szerepel,')
print(f'A hívás hossza: {mpszamlalo} másodperc.')