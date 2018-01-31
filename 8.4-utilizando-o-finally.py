
# Independente de erros, e necessario
# que seja executado um conjunto de 
# instrucoes

# Fechar acesso ao banco de dados

# Liberar recursos do sistema

# Informar que o programa concluir
# a execucao.

lista = [1, 3, 4]

try:
    print lista[12]
except IndexError, error:
    print 'Ocorreu um erro: %s' % error
finally:
    print 'Liberando recursos finais'