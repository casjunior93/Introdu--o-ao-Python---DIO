def contador_letras(lista):
    contador = []
    for x in lista:
        quantidade = len(x)
        contador.append(quantidade)

    return contador

def teste():
    return 'teste'

if __name__ == '__main__':
    lista = ['cao', 'gato']
    print(contador_letras(lista))