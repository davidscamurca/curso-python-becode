arquivo_gravacao = open('arquivo-gravacao.txt','wb')

arquivo_gravacao.write(("PYTHON E LIBERDADE").encode())
arquivo_gravacao.close()

arquivo = open('arquivo-gravacao.txt','rb')
print (arquivo.read())