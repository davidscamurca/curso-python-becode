import os

for f in os.listdir(r'/opt/Python-3.6.3'):
    n = os.path.join(r'/opt/Python-3.6.3', f)
    if os.path.isdir(n):
        print ('Diretório: %s' % n)

    if os.path.isfile(n):
        print ('Arquivo: %s' % n)
