# Estender funcionalidades da classe.

# Classe BASE

# Classe DERIVADA

class BASE:
    def Dobro(self, valor):
        return valor * 2


class DERIVADA(BASE):
    def Calcular(self, valor):
        return BASE.Dobro(self,valor)

c = DERIVADA()
print c.Calcular(2)