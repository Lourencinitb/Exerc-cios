tupla = (2, 1, 2, 2, 8, 3, 5, -1, -2, -5)

#a) Quantidade de números ímpares
def impares(tupla):
    if not tupla:
        return 0

    impar = (tupla[0] < 0)

    if impar:
        return 1 + impares(tupla[1:])
    else:
        return impares(tupla[1:])
print ("Quantidade de números ímpares: ", impares(tupla[0:]))