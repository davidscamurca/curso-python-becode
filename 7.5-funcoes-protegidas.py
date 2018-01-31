
class Secreta:

    def _init_(self):
        print "Objeto criado."

    def _funcao_protegida(self):
        print "Nao me chame."

s = Secreta()
s._funcao_protegida()