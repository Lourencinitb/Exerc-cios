numa = int(input("Digite número de A: "))
numb = int(input("Digite número de B: "))
numc = int(input("Digite número de C: "))
numd = int(input("Digite número de D: "))
numcd = numc + numd
numab = numa + numb
numcd = numc + numd

if numb > numc:
    print("B é maior que C")
    if numd > numa:
        print("D é maior que A")
        if numcd > numab:
            print("A soma de C e D é maior que a soma de A e B")
            if numc and numd > 0:
                print("C e D são números positivo")
                if (numa)%2 == 0:
                    print("Valores aceitos")
else:
    print("Valores não aceitos")