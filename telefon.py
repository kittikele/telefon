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

