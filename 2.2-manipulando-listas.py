# funcao append - adicionar

lista = ['dsc','2018']

lista.append('1')

lista.append('david')

print lista

# Acessar item
print lista[-1]

# Remover item
# lista.remove('1') != lista.remove(1)
# A linha cima esta buscando o caracter 1
# para remover e nao o indice 1 xD

# Acessar parte dos itens
lista.append('trinta e tres')
lista.append(33)
print lista

print lista[0:-1] # do segundo ao ultimo
print lista[0:] # a partir do primeiro
print lista[:-2] # do primeiro ate o penultimo

# Exercitando

li = [10, 1, 3, 'a', '$']

print li

print li[1:-2]
print li[:]
print li[0:2]









