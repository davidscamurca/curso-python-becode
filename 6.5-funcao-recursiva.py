def soma_dez(valor1):
    if valor1 < 100:
        return soma_dez(valor1+10)
    return valor1

print soma_dez(1)