#numeros primos
#itera de 1 até 101
for num in range(101):

    #verifica se o número é primo
    div = 0

    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div += 1

    if div == 2:
        print('{}'.format(num))
