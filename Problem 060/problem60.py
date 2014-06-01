# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
# and concatenating them in any order the result will always be prime. For example,
# taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792,
# represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate
# to produce another prime.
from time import time
from utils import SuperPrime, digitNumber, prime


def test_property(pr_set, n):
    global pc

    if not pc.prime(n):
        return False

    log_n = digitNumber(n)
    for a in pr_set:
        log_a = digitNumber(a)

        if not pc.prime(a*(10**log_n) + n):
            return False
        if not pc.prime(n*(10**log_a) + a):
            return False

    return True


def find_set(current_set, start_i, pl):
    if len(current_set) == 5:
        return current_set

    ws = current_set[:]
    for i in range(start_i, len(pl)):
        if test_property(ws, pl[i]):
            tmp = find_set(ws + [pl[i]], i+1, pl)

            if tmp != []:
                return tmp

    return []


def sum_list(l):
    s = 0
    for i in l:
        s += i
    return s


# **************************************************
def tests():
    print("True = %s" % test_property([3, 7, 109], 673))
    print("False = %s" % test_property([3, 7, 109], 674))
    print("True = %s" % test_property([], 3))
    print("True = %s" % test_property([], 3))


# **************************************************
start_time = time()

lim = 10000
pc = SuperPrime(lim**2)

pl = [2]
for n in range(3, 10000, 2):
    if pc.prime(n):
        pl.append(n)
# print(len(pl))

print(time() - start_time)
start_time = time()

# tests()

result = find_set([], 0, pl)
print(result)
print(sum_list(result))


print(time() - start_time)

