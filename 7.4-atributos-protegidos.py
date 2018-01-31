
# Os atribuos protegidos
# So podem ser acessados
# Somente por funcoes da classe.


class Secreta:
    __privado = None
    
    def __init__(self):
        self.__privado = 123

    def mostrar(self):
        print self.__privado

s = Secreta()

print s.mostrar()
    