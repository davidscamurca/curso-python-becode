
# Cuida de problemas durante a execucao.

# E possivel fazer continuar a execucao.

# Informa o que esta acontecendo.

lista = [1, 3, 4]
try:
    print lista[12]
except IndexError:
    print 'IndexError'