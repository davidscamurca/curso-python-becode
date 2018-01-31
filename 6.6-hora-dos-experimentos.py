

nome1 = 'Jose Maria'
nome2 = 'Maria Jose'

print 'Nome do pai: %s' % nome1
print 'Nome da mae: %s' % nome2

def nome_parente(parentesto, nome):
    print 'Nome do {a} %s: %s' % (parentesto, nome)

nome_parente('Pai','Jose Maria')
nome_parente('Mae','Maria Jose')

# Usar quando um determinado bloco de codigo
# Se repete duas ou mais vezes.

def parametro_default(dia, mes='1'):
    print 'Dia %s Mes %s' % (dia, mes)

parametro_default(1)