#!/bin/env python3


lim = 200
coin = [1, 2, 5, 10, 20, 50, 100, 200]
p = [0] * (lim + 1)
p[0] = 1
p[1] = 1
    
for v in coin:
    for i in range(v, lim+1):
        if (i - v) > 0:
            p[i] += p[i-v]
            
print(p[lim])
print(p[:10])