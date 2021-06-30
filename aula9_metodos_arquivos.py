#biblioteca python
import shutil

def escrever_arquivo(texto):
    arquivo = open('arquivos/teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas])/4
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copiar_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '/home/carlos/Documentos/Introdução-ao-Python-DIO/arquivos2')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '/home/carlos/Documentos/Introdução-ao-Python-DIO/arquivos')

if __name__ == "__main__":
    #escrever_arquivo('Primeira linha\n')
    #aluno = 'Carlos,9,10,8\n'
    #atualizar_arquivo('arquivos/notas.txt',aluno)
    #ler_arquivo('arquivos/teste.txt')
    #media_notas('arquivos/notas.txt')
    #copiar_arquivo('arquivos/notas.txt')
    move_arquivo('arquivos/teste.txt')