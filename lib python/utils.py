from math import *

# teste la primarite du nombre passe en parametre
def prime(n):
    if n == 2:
        return True

    if n < 2 or not n % 2:
        return False

    lim = n ** 0.5
    i = 3
    while i <= lim:
        if not n % i:
            return False

        i += 2

    return True


class SuperPrime():
    """
        Keep track of previously results. Usefull if we have to test
        again and again the same numbers.

        Very simple, and possibly dangerous (if n > size for example)
    """
    def __init__(self, size):
        self.prime_list = size*[-1]

    def prime(self, n):
        if self.prime_list[n] == -1:
            self.prime_list[n] = prime(n)

        return self.prime_list[n]

def fact(n):
    for i in range(n-1, 0, -1):
        n *= i

    return n

# Supprime les doublons de la liste passee en parametre
def uniq(list):
    list.sort()

    size = len(list)
    i = 0
    while i < size - 1:
        if list[i] == list[i+1]:
            del list[i]
            size -= 1
            continue

        i += 1

    return list


# transforme un entier en liste contenant tout ses chiffres
def toList(n):
    result = []

    while n > 0:
        result.append(n%10)
        n //= 10

    result.reverse()

    return result

   
# Teste si le nonbre est un palyndrome
def palindrome(string):
    a = 0
    b = len(string) -1

    while a < b:
        if string[a] != string[b]:
            return False

        a += 1
        b -= 1

    return True


def reverseString(string):
    return string[::-1]



def digitsSum(n):
    sum = 0

    while n > 0:
        sum += n % 10
        n //= 10

    return sum


def digitNumber(n):
    total = 0

    while n > 0:
        total += 1
        n //= 10

    return total
   


# ******************************************************************************

class sortedList(object):

    def __init__(self, list):
        self.list = []
        for i in list:
            self.add(i)
            # self.show()

    # Ajoute la liste passee en parametre
    def addList(self, list):
        for i in list:
            self.add(i)

    # Ajoute le nombre passe en parametre a la liste
    def add2(self, n):
        # print("Adding %d to the list" % n)
        if len(self.list) == 0 or n > self.list[-1]:
            self.list.append(n)
            return 1

        a = 0
        b = len(self.list) - 1

        while True:
            i = (a + b)//2

            di = n - self.list[i]

            if di == 0:#n deja dans la liste\
                # print("deja dans la liste", n)
                return 0

            if a == i:#a+1 == b
                if self.list[a] > n:
                    self.list.insert(a, n)
                    return 1
                else:
                    self.list.insert(a+1, n)
                    return 1

            if di > 0:
                a = i
            elif di < 0:
                b = i

    def add(self, n):
        a = 0
        b = len(self.list) - 1

        while a <= b:
            i = (a + b) // 2

            if self.list[i] == n:
                return False

            if self.list[i] < n:
                a = i + 1
                continue

            b = i - 1

        self.list.insert(a, n)
        return True

    def __contains__(self, n):
        # print("Teste l'appartenance de %d" % n)
        a = 0
        b = len(self.list) - 1

        while a <= b:
            i = (a + b) // 2

            if self.list[i] == n:
                return True

            if self.list[i] < n:
                a = i + 1
                continue

            b = i - 1

        return False


    # Retourne l'index du nombre
    # retourne -1 si le nombre n'appartient pas la liste
    def index(self, n):
        a = 0
        b = len(self.list) - 1

        while a <= b:
            i = (a + b) // 2

            if self.list[i] == n:
                return i

            if self.list[i] < n:
                a = i + 1
                continue

            b = i - 1

        return -1

    def __add__(self, stranger):
        newList = sortedList([])
        newList.list = self.list.copy()

        for i in stranger.list:
            newList.add(i)

        return newList


    def __len__(self):
        return len(self.list)

    def __getitem__(self, i):
        return self.list[i]

    def show(self):
        print(self.str())

    def str(self):
        return str(self.list)

    def __str__(self):
        return str(self.list)

    def __len__(self):
        return len(self.list)

    def size(self):
        return len(self.list)



    # Renvoie la somme de tout les elements de la liste
    def sum(self):
        result = 0

        for i in self.list:
            # print(i)
            result += i

        return result

    # Verifie que la liste est bien triee et ne contient aucun doublons
    def sorted(self):
        for i in range(len(self.list) - 1):
            if self.list[i] >= self.list[i+1]:
                return False

        return True


# ******************************************************************************

class fraction:

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
        self.simplifie()


    def __add__(self, frac):
        self.a *= frac.b
        self.a += frac.a * self.b
        self.b *= frac.b

        # self.simplifie()

        return self


    def __sub__(self, frac):
        self.a *= frac.b
        self.a -= frac.a * self.b
        self.b *= frac.b

        # self.simplifie()

        return self


    def __mul__(self, frac):
        self.a *= frac.a
        self.b *= frac.b

        # self.simplifie()

        return self


    def __truediv__(self, frac):
        self.a *= frac.b
        self.b *= frac.a

        # self.simplifie()

        return self


    def __str__(self):
        return str(self.a) + '/' + str(self.b)


    def simplifie(self):
        while not self.a % 2 and not self.b % 2:
            self.a //= 2
            self.b //=2

        i = 3
        lim = sqrt(self.a)
        while i <= lim:
            if not self.a % i and not self.b % i:
                self.a //= i
                self.b //= i
                lim = sqrt(self.a)
                i = 3

            i += 2


    def inverse(self):
        (self.a, self.b) = (self.b, self.a)








