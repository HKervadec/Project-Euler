import math

def gen_stats(max, power):
    tab = max*[0]

    i = 1

    while True:
        cube = i**power

        if cube >= 10**max:
            break

        pos = math.floor(math.log10(cube))
        tab[pos] += 1
        # print(cube, pos)

        i += 1

    return tab


max = 20
max_cube = 5
stats = (max_cube + 1)*[0]

for n in range(2, max_cube+1):
    stats[n] = gen_stats(max, n)

for i in range(max):
    line = "[10^%d:10^%d] " %(i, i+1)

    for n in range(2, max_cube+1):
        line += "%d " % stats[n][i]

    print(line)