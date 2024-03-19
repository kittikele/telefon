f = open('hivas.txt', 'rt', encoding='utf-8')

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

