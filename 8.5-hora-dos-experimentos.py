
lista = [1,2]

try:
    print (f)
    print (lista[11])
except IndexError:
    print ('Error no index')
    pass
except:
    print ('Erro generico')
    pass
finally:
    print ('Pasando por finally')
    pass

    # RAISE, dispara a descricao da excessao.
    # PASS, sai da exessao e nao mostra nada.
    # FINALLY, fechar, finalizar algo independente do que acontenca.
print ('Continuando')