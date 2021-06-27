lista = [15, 3, 5,7]
lista_animais = ['cachorro', 'gato', 'elefante', 'rato']

print(lista_animais[2])

print(sum(lista)) #16
print(max(lista)) #7
print(min(lista)) #1

print(min(lista_animais)) #cachorro
print(max(lista_animais)) #rato

print('gato' in lista_animais) #True
print('lobo' in lista_animais) #False

#multiplica a quantidade dos valores na lista
nova_lista = lista_animais * 3
print(nova_lista) #print('gato' in lista_animais)

#adiciona na lista
lista_animais.append('lobo')
print(lista_animais) #print('gato' in lista_animais)

#retirar da lista
lista_animais.pop()
print(lista_animais) #print('gato' in lista_animais)

lista_animais.pop(0)
print(lista_animais) #print(lista_animais)

lista_animais.remove('elefante')
print(lista_animais) #print(lista_animais)

#ordenar lista
lista.sort()
lista_animais.sort()

print(lista)
print(lista_animais)

lista.reverse()
lista_animais.reverse()

print(lista)
print(lista_animais)