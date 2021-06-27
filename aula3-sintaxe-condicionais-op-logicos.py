a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

# if a > b:
#     print('{} maior que {}'.format(a,b))
# elif a < b:
#     print('{} maior que {}'.format(b,a))
# elif a == b:
#     print('Mesmo número digitado: {}'.format(a))

# c = int(input("Terceiro valor: "))
# if a > b and a > c:
#     print('O maior número é  {}'.format(a))
# elif b > a and b  > c:
#     print('O maior número é  {}'.format(b))
# else:
#     print('O maior número é  {}'.format(c))

resto = a % 2
if resto == 0:
    print('Numero {} é par'.format(resto))
else:
    print('Numero {} é impar'.format(resto))