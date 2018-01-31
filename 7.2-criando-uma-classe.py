class Retangulo:
    lado_a = None
    lado_b = None

    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
        print "Nova instancia retangulo."

    def calcula_area(self):
        return self.lado_a * self.lado_b

    def calcula_perimetro(self):
        return 2*self.lado_a + 2*self.lado_b

r1 = Retangulo(12,15)
print r1.calcula_area()
print r1.calcula_perimetro()

class Celular:
    marca = None
    modelo = None
    ano = None

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def mostra(self):
        print self.marca, self.modelo, self.ano


c = Celular('Apple','iPhoneX','2017')
c.mostra()