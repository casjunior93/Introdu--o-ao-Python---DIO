contador_letras = lambda lista: [len(x) for x in lista]

lista = ['cao', 'gato']
print(contador_letras(lista))

soma = lambda a, b: a + b
sub = lambda a, b: a - b
print(soma(5,10))
print(sub(10,5))

#dicionario de funçoes lambdas

calculadora = {
    'soma': lambda a, b: a + b,
    'sub' : lambda a, b: a - b,
    'mult' : lambda a, b: a * b,
    'div' : lambda a, b: a / b
}

soma = calculadora['soma']
mult = calculadora['mult']
sub = calculadora['sub']
div = calculadora['div']

print(soma(10,5))
print(mult(10,5))
print(sub(10,5))
print(div(10,5))