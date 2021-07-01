#exce ption hierarchy
lista = [1,10]
try:
    arquivo = open('arquivos/notas.txt', 'r')
    divisao = 10/1
    numero = lista[1]
    x = 1
#começa pelas exceções mais baixas
except ZeroDivisionError:
    print('Não é possível realiza uma divisão por zero.')
except IndexError:
    print('Índice inválido')
except BaseException as ex:
    print("Erro desconhecido: {}".format(ex))#name 'a' is not defined
else:
    print('Não houve exceção')
finally:
    print('Sempre executa')
    arquivo.close()