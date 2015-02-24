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