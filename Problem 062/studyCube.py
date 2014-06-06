import math

def gen_stats(max):
    tab = (math.floor(math.log10(max))+1)*[0]

    i = 1

    while True:
        cube = i**3

        if cube >= max:
            break

        pos = math.floor(math.log10(cube))
        tab[pos] += 1
        # print(cube, pos)

        i += 1

    return tab


max = 10000000000000
stats = gen_stats(max)

for i in range(math.floor(math.log10(max))):
    print("[10^%d:10^%d] %d" %(i, i+1, stats[i]))