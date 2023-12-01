class HaromszogEgyenlotlenseg():
    def haromszog_egyenlotlenseg_vizsgalo(self, a, b, c):
        if type(a) not in [int, float] or type(b) not in [int, float] or type(c) not in [int, float]:
            raise TypeError("Csak int vagy float típus fogadható el!")

        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False

    def vizsgalat(self, a, b, c):
        e = HaromszogEgyenlotlenseg()
        eredmeny = e.haromszog_egyenlotlenseg_vizsgalo(a,b,c)

        print(f"Háromszög egyenlőtlenség vizsgálat az alábbi oldalhosszokkal: a = {a}, b = {b} és c = {c}")

        if eredmeny:
            print("Ezekből az oldalhosszakból háromszög készíthető.")
        else:
            print("Ezekből az oldalhosszakból nem lehet háromszöget készíteni.")

e = HaromszogEgyenlotlenseg()
e.vizsgalat(2,2,5)
e.vizsgalat(3,3,5)
e.vizsgalat(4,4,8)
e.vizsgalat(5,5,15)
