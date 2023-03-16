print('-'*30)
print('Questão 2 - Referente a sequência de Fibonacci.')
print('-'*30)
n = int(input('\nDigite um número: '))
t1 = 0
t2 = 1

# Números menores do que 3
print('-'*30)
if (n <= 1):
    print('\nNesse caso aplicando o teorema da sequência de Fibonacci especificado na questão, e o número oferecido sendo menor do que 3 o resultado será:')
    print('{} ->'.format(t1), end='')

elif (n == 2):
    print('\nNesse caso aplicando o teorema da sequência de Fibonacci especificado na questão, e o número oferecido sendo menor do que 3, o resultado será:')
    print('{} -> {}'.format(t1, t2), end='')

# Númeres maiores do que 3
else:
    print('\nNesse caso aplicando o teorema da sequência de fibonacci especificado na questão, e o número oferecido sendo maior do que 3, temos a sequência: ')
    print('{} -> {}'.format(t1, t2), end='')
    cont = 3
    while cont <= n:
        t3 = t1 + t2
        print(' -> {}'.format(t3), end='')
        t1 = t2
        t2 = t3
        cont += 1

# Verificação se o número oferecido pertence a sequência
if (n == t1):
    print('\nO número oferecido FAZ parte da sequência.')

else:
    print('\nO número oferecido NÃO faz parte da sequência.')
    print('Fim do programa...')
