#modulos são arquivos .py
from  aula7_televisao import Televisao
from  aula7_calculadora import Calculadora
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':

    televisao = Televisao()
    televisao.power()

    print(televisao.ligada)

    calculadora = Calculadora()

    print(calculadora.soma(10,2))

    lista = ['cao', 'elefante']
    print(contador_letras(lista))

    print(teste())