import os

f = open('aula10-8/file2.txt','w')
# gravando item
f.write('gravando info no file')
f.close()

if os.path.exists('aula10-8/file2.txt'):
    f = open('aula10-8/file2.txt','r')
    print (f.read())
    f.close()
else:
    print ('Arquivo nao encontrado.')


print (os.path.curdir)
print (os.path.abspath(os.path.curdir))
print (os.path.join(os.path.abspath(os.path.curdir),'outro-diretorio','nome-arquivo.txt'))

print (os.listdir('.'))

print (os.path.isdir('aula10-8'))
print (os.path.isfile('modulo.py'))