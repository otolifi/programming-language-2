import random

def sorteia_times():
    m = random.randrange(1,10)
    v = random.randrange(1,10)
    return [m,v]

jogos = []
for i in range(10):
    ml = []
    vl = []
    for i in range(5):
        m = 0
        v = 0
        while m == v and (m not in ml) and (m not in vl) and (v not in vl) and (v not in ml) and ([m,v] not in jogos) and ([v,m] not in jogos):
            m = random.randrange(1,10)
            v = random.randrange(1,10)
            jogo = [m, v]
            if m != v and (m not in ml) and (m not in vl) and (v not in vl) and (v not in ml) and ([m,v] not in jogos) and ([v,m] not in jogos):
                ml.append(m)
                vl.append(v)
        jogos.append(jogo)
print(jogos)
print(ml)
print(vl)

for jogo in jogos:
    print(f"{jogo[0]}")
print('-----')
for jogo in jogos:
    print(f"{jogo[1]}")



    