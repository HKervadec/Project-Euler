#!/usr/bin/env python3

# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are 
# all figurate (polygonal) numbers and are generated by the following formulae:
# Triangle 	  	P3,n=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
# Square 	  	P4,n=n^2 	  	1, 4, 9, 16, 25, ...
# Pentagonal 	  	P5,n=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
# Hexagonal 	  	P6,n=n(2n−1) 	  	1, 6, 15, 28, 45, ...
# Heptagonal 	  	P7,n=n(5n−3)/2 	  	1, 7, 18, 34, 55, ...
# Octagonal 	  	P8,n=n(3n−2) 	  	1, 10, 21, 40, 65, ...

# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting 
# properties.

    # The set is cyclic, in that the last two digits of each number is the first 
    # two digits of the next number (including the last number with the first).
    # Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal 
    # (P5,44=2882), is represented by a different number in the set.
    # This is the only set of 4-digit numbers with this property.

# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each 
# polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, 
# is represented by a different number in the set.

from time import time


def find_set(current_set, remaining_prop):
    if not True in remaining_prop:
        if is_next(current_set[-1], current_set[0]):
            return current_set
        else:
            return []

    for i in range(len(remaining_prop)):
        if remaining_prop[i]:
            for k in lists[i]:
                if current_set == [] or is_next(current_set[-1], k):
                    arp = remaining_prop[:]
                    arp[i] = False

                    tmp = find_set(current_set + [k], arp)

                    if tmp:
                        return tmp

    return []


def is_next(a, b):
    return a % 100 == b // 100


def sum_list(l):
    s = 0
    for i in l:
        s += i
    return s


# *******************************************************************
def tests():
    print("True = %s" % is_next(8128, 2882))
    print("True = %s" % is_next(2882, 8281))
    print("True = %s" % is_next(8281, 8128))
    print("False = %s" % is_next(8281, 7128))
    print("False = %s" % is_next(8128, 2881))

    print("8128, 2882, 8281")
    print(find_set([], [True, True, True, False, False, False]))


# *******************************************************************
# tests()

start_time = time()

triangle = lambda n: n*(n+1)//2
square = lambda n: n**2
pentagonal = lambda n: n*(3*n-1)//2
hexagonal = lambda n: n*(2*n - 1)
heptagonal = lambda n: n*(5*n - 3)//2
octagonal = lambda n: n*(3*n - 2)


list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []

generators = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]
lists = [list3, list4, list5, list6, list7, list8]

for i in range(len(generators)):
    n = 0
    r = 0
    while r < 10000:
        r = generators[i](n)

        if 1000 <= r < 10000:
            lists[i].append(r)

        n += 1

# for l in lists:
#     print(len(l))



result = find_set([], 6*[True])
print(result)
print(sum_list(result))


print(time() - start_time)