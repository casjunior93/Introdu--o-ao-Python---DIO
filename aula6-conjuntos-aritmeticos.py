conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
print(type(conjunto)) #<class 'set'>

conjunto.add(5)
print(conjunto) # {1, 2, 3, 4, 5}
conjunto.discard(2)
print(conjunto) # {1, 3, 4, 5}

#união dos conjuntos
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao) #{1, 3, 4, 5, 6, 7, 8}

#intersecção dos conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao) #{5}

#diferença - números que só existem no primeiro conjunto
conjunto_diferenca = conjunto.difference(conjunto2)
print(conjunto_diferenca) #{1, 3, 4}
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(conjunto_diferenca2) #{8, 6, 7}

#diferenca simetrica - apenas os elementos que estiverem nos dois sets, porém que não se repitam, serão exibidos.
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_dif_simetrica) #{1, 3, 4, 6, 7, 8}

###pertinencia - 
#se conjunto é subconjunto de outro
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset) #True

#se é o superconjunto de um conjunto
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset) #True

#converter lista para conjunto
lista = ['cao', 'gato', 'rato', 'elefante', 'cao']
print(str(len(lista)) + " oi")
#remover duplicidade
conjunto_animais = set(lista)
print(type(conjunto_animais)) #<class 'set'>
print(conjunto_animais) #{'elefante', 'rato', 'cao', 'gato'}

lista_animais = list(conjunto_animais)
print(lista_animais) #['cao', 'elefante', 'gato', 'rato']



