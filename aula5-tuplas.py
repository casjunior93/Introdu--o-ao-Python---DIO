#imutável

tupla = (1,10,12,14)
print(tupla)

print(tupla[2]) #12
print(len(tupla)) #4

lista = ['carlos', 'alberto']
tupla_nomes = tuple(lista)

print(type(tupla_nomes)) #print(tupla[2])

lista2 = list(tupla_nomes)
print(type(lista2))