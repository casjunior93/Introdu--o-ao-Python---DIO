#abre um arquivo ou cria se não existe com w, a
arquivo = open('arquivos/teste1.txt', 'w')
#w sobrepõe o que está escrito
#a - atualiza

arquivo.write('Primeira linha')
arquivo.write('\nSegunda linha')
arquivo.close()