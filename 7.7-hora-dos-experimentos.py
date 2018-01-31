
class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def calcula_area(self):
        return self.ladoA * self.ladoB

class RetanguloExtend(Retangulo):
    def calcula_perimetro(self):
        return 2*self.ladoB + 2*self.ladoB

r = Retangulo(2,3)
r2 = RetanguloExtend(4,4)

print r.calcula_area()

print r2.calcula_perimetro()