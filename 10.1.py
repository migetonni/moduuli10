

class hissi:

    def __init__(self,ylinkerros, alinkerros):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.kerros = 0



    def kerros_ylos(self):
        if self.kerros < self.ylinkerros:
            self.kerros += 1
            print(f"Kerros on {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alinkerros:
            self.kerros -= 1
            print(f"Kerros on {self.kerros}")

    def siirry_kerrokseen(self, haluttu_kerros):
        if self.kerros < haluttu_kerros:
            while self.kerros < haluttu_kerros:
                self.kerros_ylos()
        elif self.kerros > haluttu_kerros:
            while self.kerros > haluttu_kerros:
                self.kerros_alas()




hissukka = hissi(8,1)

hissukka.siirry_kerrokseen(6)
hissukka.siirry_kerrokseen(1)








