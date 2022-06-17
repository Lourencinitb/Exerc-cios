import statistics as st
y = []
def entrada(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.strip('-').isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = entrada("Digite 1° número: "), entrada("Digite 2° número: "), entrada("Digite 3° número: "), entrada("Digite 4° número: "), entrada("Digite 5° número: "), entrada("Digite 6° número: ")

    
for i in n:
        if i > 0:
            y.append(i)

print(f'\n{len(y)} valores positivos | Média dos valores {y} = {st.mean(y)}')