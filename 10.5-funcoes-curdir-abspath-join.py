import os

# Mostra o diretorio atual.
print (os.path.curdir)

# Mostra o caminho absoluto do firetorio atual.
print (os.path.abspath(os.path.curdir))

print (os.path.join(os.path.abspath(os.path.curdir))+'/arquivo-gravacao.txt')


