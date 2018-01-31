import os

if (os.path.exists('arquivo-gravacao.txt')):
    arquivo = open('arquivo-gravacao.txt','r')
    print (arquivo.read())
    arquivo.close()
else:
    print ('Arquivo nao encontrado')

